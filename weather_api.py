import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_KEY = "1f17c51fe3c69e2ece157c8a20702013"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        "temperature": data["main"]["temp"] if "main" in data else None,
        "humidity": data["main"]["humidity"] if "main" in data else None,
        "description": data["weather"][0]["description"] if "weather" in data else None
    }
    return weather

def get_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]["lat"], data[0]["lon"]
    return None, None

def get_historical_weather(city):
    lat, lon = get_coordinates(city)
    if lat is None:
        return []

    historical_data = []
    today = datetime.utcnow()

    for i in range(5):
        day = today - timedelta(days=i)
        timestamp = int(day.timestamp())
        url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()

        if "current" in data:
            temp = data["current"]["temp"]
            humidity = data["current"]["humidity"]
            historical_data.append({
                "date": day.strftime('%Y-%m-%d'),
                "temperature": temp,
                "humidity": humidity
            })

    return historical_data[::-1]  # return in chronological order

def plot_weather_trends(historical_data):
    if not historical_data:
        return

    dates = [entry["date"] for entry in historical_data]
    temps = [entry["temperature"] for entry in historical_data]
    humidities = [entry["humidity"] for entry in historical_data]

    plt.figure(figsize=(6, 4))
    plt.plot(dates, temps, marker='o', label='Temperature (°C)', color='tomato')
    plt.plot(dates, humidities, marker='s', label='Humidity (%)', color='steelblue')
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Historical Weather Trends (Past 5 Days)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/weather_trends.png")
    plt.close()
