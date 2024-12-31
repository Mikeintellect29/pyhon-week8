import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    # Construct the API request URL
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"  # Units in metric (Celsius)
    
    try:
        # Make the GET request
        response = requests.get(url)
        data = response.json()
        
        # Check the status code
        if response.status_code == 200:
            # Extract weather data
            main_data = data["main"]
            weather_data = data["weather"][0]
            wind_data = data["wind"]
            sys_data = data["sys"]

            temperature = main_data["temp"]
            feels_like = main_data["feels_like"]
            humidity = main_data["humidity"]
            weather_description = weather_data["description"]
            wind_speed = wind_data["speed"]
            wind_deg = wind_data["deg"]
            sunrise = datetime.utcfromtimestamp(sys_data["sunrise"]).strftime('%H:%M:%S')
            sunset = datetime.utcfromtimestamp(sys_data["sunset"]).strftime('%H:%M:%S')

            # Display weather information
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_description.capitalize()}")
            print(f"Wind: {wind_speed} m/s at {wind_deg}°")
            print(f"Sunrise: {sunrise} UTC")
            print(f"Sunset: {sunset} UTC")
        
        else:
            # Print error message from API response
            print(data.get("message", "City not found. Please check the name and try again."))
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Get user input
city = input("Enter city name: ").strip().title()
get_weather(city)
