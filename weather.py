print("\n MINI PRO DAY9 2")
import requests
import json
from datetime import datetime

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather_info
    else:
        return {"error": data.get("message", "Unable to fetch weather data")}

def save_weather(weather_info, filename="weather_data.json"):
    try:
        with open(filename, "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []

    history.append(weather_info)

    with open(filename, "w") as file:
        json.dump(history, file, indent=4)
