import speech
import requests

def headlines():
    # Set API endpoint and parameters
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'in',  # Set country parameter to US
        'apiKey': '98109c5d509c42a19e4a4c6409df05cb'  # Replace with your NewsAPI API key
    }

    # Send GET request to API endpoint
    response = requests.get(url, params=params)

    # Parse response JSON data
    data = response.json()
    c = 1
    # Print each article's title
    for article in data['articles']:
        if c == 11:
            break
        print(article['title'])
        speech.speech(article['title'])
        c+=1
        print("\n")                