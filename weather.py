import requests
import speech
# Set your OpenWeatherMap API key and the city you want to get the weather for
def forecast(city):        
    api_key = 'YOUR API KEY'
    # Set the API endpoint URL and parameters
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Send a GET request to the API endpoint and parse the response JSON
    response = requests.get(url)
    data = response.json()

    # Extract the current temperature in Celsius from the response data
    temp_celsius = str(float(data['main']['temp']))
    # Print the current temperature in Celsius
    print("The current temperature at " + city + " is " + temp_celsius + " degree Celcius")
    speech.speech("The current temperature at " + city + " is " + temp_celsius + " degree Celcius")
