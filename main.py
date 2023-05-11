from __future__ import print_function
import os
import speech_recognition as sr
import search
import music
import notes
import speech
import socials
import news
import getCalendar
import weather
import pyjokes
import capture_record
def get_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

WAKE_WORD = "vanilla"
SERVICE = getCalendar.authenticate()
print("Listening....")
CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
MUSIC_STRS = ["play a song", "open a song"]
NEWS_STRS = ["show headlines", "what is the news", "what's in the news"]
SEARCH_STRS = ["search something", "i want to know something", "i have a query"]
WEATHER_STRS = ["what is the current weather at", "can you tell the present weather at", "what is the forecast of"]
SOCIALS_STR = ["open socials", "i want to send a message", "let me see my social media"]
JOKES_STRS = ["tell me some jokes", "say something funny", "make me laugh"]
PICTURE_STRS = ["capture a pic", "take a picture", "click a pic", "click a picture"]
VIDEO_STRS = ["record a video", "film a video", "record me"]
while True:
    text = get_input()
    if "what is your name" in text:
            speech.speech("Hi! My name is Vanilla. Nice to meet you!!")
            speech.speech("I am a virtual voice assistant here to make your lives easier!")
            speech.speech("Say the word help if you want to find out what commands to say.")
    HELP_STRS = [CALENDAR_STRS, NOTE_STRS, MUSIC_STRS, NEWS_STRS, SEARCH_STRS, WEATHER_STRS, SOCIALS_STR, JOKES_STRS, PICTURE_STRS, VIDEO_STRS]
    TOPIC_STRS = ["to view your schedule", "to make a note", "to listen to music", "to get the news headlines", "to search anything in the internet", "to check the weather of any city", "to check your social media", "to listen to a joke", "to capture a picture", "to record a video"]
    size = len(TOPIC_STRS)
    if "help" in text:
        speech.speech("Say vanilla to activate me")
        print("Say vanilla to activate me\n")
        for i in range(0,size):
            speech.speech("Use any of the following commands " + TOPIC_STRS[i])
            print(TOPIC_STRS[i] + "\n")
            ln = len(HELP_STRS[i])
            x = 1
            for j in range(0,ln):
                print(str(x) + ". " + HELP_STRS[i][j] + "\n")
                x = x+1
        print("Listening...")
                


    if(text.count(WAKE_WORD)) > 0:
        speech.speech("Listening now")
        print("Listening....")
        text = get_input()
        if "hello" in text:
            speech.speech("Hello! How are you?")

        


        
        for phrase in CALENDAR_STRS:
            if phrase in text:
                date = getCalendar.date(text)
                if date:
                    getCalendar.get_events(date, SERVICE)
                else:
                    speech.speech("Please Try Again")



        
        for phrase in NOTE_STRS:
            if phrase in text:
                speech.speech("What would you like me to write down? ")
                note = get_input()
                notes.make_note(note)


        

        for phrase in MUSIC_STRS:
            if phrase in text:
                speech.speech("What would you like to listen?")
                print("Listening...")
                song = get_input()
                music.play(song)

        
        for phrase in NEWS_STRS:
            if phrase in text:
                news.headlines()
                print("Listening...")
        
        
        for phrase in SEARCH_STRS:
            if phrase in text:
                speech.speech("What would you like me to search?")
                print("Listening...")
                query = get_input()
                search.find(query)
                print("Listening...")
       
        for phrase in WEATHER_STRS:
            if phrase in text:
                city = text.split(" ")[-1]
                weather.forecast(city)
                print("Listening...")
        
        SOCIAL_MEDIA = ["whatsapp", "instagram", "github", "linkedin", "medium"]
        for phrase in SOCIALS_STR:
            if phrase in text:
                speech.speech("What would you like to access? Choose from the following. 1. Whatsapp. 2. instagram. 3. Github. 4. LinkedIn. 5. Medium.")                
                print("Listening...")
                social = get_input()
                if social in SOCIAL_MEDIA:
                    speech.speech("Opening " + social + " now")
                    socials.open(social)
                else:
                    speech.speech("Sorry. I am not authorised to access this account")
                print("Listening...")
        
        for phrase in JOKES_STRS:
            if phrase in text:
                joke = pyjokes.get_joke()
                print(joke + "\n")
                speech.speech(joke)                
                print("Listening...")
        for phrase in PICTURE_STRS:
            if phrase in text:
                speech.speech("Clicking a picture now,")
                capture_record.camera()
                speech.speech("You can now view the captured picture in this folder only")
                print("Listening...")
        for phrase in VIDEO_STRS:
            if phrase in text:
                speech.speech("For how many seconds would you like to record?")
                print("Listening...")
                duration = int(get_input())
                capture_record.record(duration)
                speech.speech("You can now view the recorded video in the Pictures folder")
                print("Listening...")
        
    if  "goodbye" in text:
        speech.speech("Terminating")
        break