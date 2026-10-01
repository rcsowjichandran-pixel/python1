import sys
import weather

if len(sys.argv) < 2:
    print("Usage: python main.py <city>")
    sys.exit()

city = sys.argv[1]
info = weather.fetch_weather(city)

if "error" in info:
    print("Error:", info["error"])
else:
    print(f"City: {info['city']}")
    print(f"Temperature: {info['temperature']} °C")
    print(f"Humidity: {info['humidity']}%")
    print(f"Condition: {info['condition']}")
    weather.save_weather(info)
    print("Weather data saved to file.")
