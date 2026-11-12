import os
import httpx
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("OPENWEATHER_API_KEY")
params = {
    "q": "London",
    "appid": weather_api_key,
    "units": "metric"
}

if not weather_api_key:
    raise SystemExit("Error: OPENWEATHER_API_KEY is not set in the environment variables.")

weather = httpx.get("https://api.openweathermap.org/data/2.5/weather", params=params, timeout=10)
# print(weather.status_code)
# print(weather.text)
weather.raise_for_status()


data = weather.json()
print(f"{data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}")

# {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 4.84, 'feels_like': 1.9, 'temp_min': 3.12, 'temp_max': 5.98, 'pressure': 1009, 'humidity': 78, 'sea_level': 1009, 'grnd_level': 1007}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 21, 'gust': 5.8}, 'clouds': {'all': 1}, 'dt': 1794511064, 'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1794467585, 'sunset': 1794500179}, 'timezone': 0, 'id': 2643743, 'name': 'London', 'cod': 200}
