#A simple weather app.
#23/7/2025
#Works well.
#Can use on pi zero.

import requests
from datetime import datetime

latitude = 53.2724
longitude = -9.051

# Open-Meteo URL with required hourly parameters
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,wind_speed_10m"
    f"&timezone=auto"
)

# Fetch data
resp = requests.get(url)
data = resp.json()

# Get current hour time string
now = datetime.now().strftime("%Y-%m-%dT%H:00")

# Extract matching hourly values
hourly = data["hourly"]
try:
    index = hourly["time"].index(now)
    temp = hourly["temperature_2m"][index]
    humidity = hourly["relative_humidity_2m"][index]
    rain_chance = hourly["precipitation_probability"][index]
    wind_speed = hourly["wind_speed_10m"][index]
    
    print(f"Temp: {temp:.1f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Rain: {rain_chance}% chance")
    print(f"Wind: {wind_speed:.1f} m/s")
    
    
except ValueError:
    print("Current hour data not available.")
