from __future__ import print_function
import os.path
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import speech
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january","february","march","april","may","june","july","august","september","october","november","december"]
DAYS = ["monday","tuesday", "wednesday", "thursday", "friday","saturday","sunday"]
DAY_EXT = ["rd", "th", "st", "nd"]

def authenticate():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service
def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    # NEW STUFF STARTS HERE
    if not events:
        speech.speech('No upcoming events found.')
    else:
        speech.speech(f"You have {len(events)} events on this day.")

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])  # get the hour the event starts
            if int(start_time.split(":")[0]) < 12:  # if the event is in the morning
                start_time = start_time = str(int(start_time.split(":")[0])) + str(int(start_time.split(":")[1])) +  "a.m."
            else:
                start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]  # convert 24 hour time to regular
                start_time = start_time + "pm"  

            speech.speech(event["summary"] + " at " + start_time)



def date(text):
    text = text.lower()
    today = datetime.date.today()


    if text.count("today") > 0:
        return today
    day=-1
    day_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word)+1
        elif word in DAYS:
            day_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXT:
                found = word.find(ext)
                if found>0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year+1
    if day < today.day and month == -1 and day != -1:
        month = month+1
    if month == -1 and day == -1 and day_week != -1:
        current_day_week = today.weekday()
        diff = day_week - current_day_week
        if diff < 0:
            diff+=7
            if text.count("next")>= 1:
                diff+=7
        return today+ datetime.timedelta(diff)
    return datetime.date(month=month, day = day, year=year)
