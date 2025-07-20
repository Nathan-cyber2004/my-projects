import requests
import json
import os

# Load secure credentials from environment variables
api_key = os.getenv("OPENWEATHER_API_KEY")

# Weather parameters
latitude = 35.42
longitude = -80.63
units = "imperial"

def get_weather_data(lat, lon, API_KEY, units):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={units}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        print("Weather data retrieved successfully.")
        with open("data.json", "w") as new_file:
            json.dump(response.json(), new_file, indent=4)
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def filter_data(data):
    if data is None:
        print("No data to filter.")
        return

    current_location = data.get("name", "Unknown Location")
    main_data = data.get("main", {})
    weather_desc = data.get("weather", [{}])[0].get("description", "No description")
    wind_data = data.get("wind", {})

    return [
        current_location,
        main_data.get("temp"),
        main_data.get("feels_like"),
        main_data.get("temp_min"),
        main_data.get("temp_max"),
        weather_desc,
        main_data.get("humidity"),
        wind_data.get("speed")
    ]

# Run and load data
try:
    data = get_weather_data(latitude, longitude, api_key, units)
    if data is None:
        raise ValueError("No data retrieved.")
except:
    print("Using backup data from file.")
    with open("data.json", "r") as file:
        data = json.load(file)

relevant_data = filter_data(data)
