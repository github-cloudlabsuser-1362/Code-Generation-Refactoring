# build in python a weather app that connects to OpenWeatherMap api and shows results fro a city 
import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in environment variables. Please set it in a .env file.")
city = input("Enter the city name: ")
params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'  # Use 'imperial' for Fahrenheit
}   
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Error: {response.status_code} - {response.text}")
    