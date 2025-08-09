# This file contains the main code logic for getting the weather data

import requests
import os
import json
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather_data(lat, lon):
  base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=imperial"
  try:
    response = requests.get(base_url)
    if response.status_code == 200:
      # with open("weather_data.json", "w") as test_file: This line creates the json file that was used to test the Agent's ability to read files
      #   json.dump(response.json(), test_file, indent = 4) It is not actually needed in this project 
      return response.json()
  except Exception as E:
    print("There was an error... " + E)

@tool
def weather_data(lat, lon):
  """This function gets weather data in imperial units and returns a dictionary"""
  data = get_weather_data(lat, lon)

  if "error" in data:
    print("There was an error with the data...")
    return data

  try:
    description = data["weather"][0]["description"]

    temperature = data["main"]["temp"]
    min_temp = data["main"]["temp_min"]
    max_temp = data["main"]["temp_max"]

    weather_dict = {"description": description, "temperature": temperature, "minimum temperature": min_temp, "maximum temperature": max_temp}
  except KeyError as KE:
    print("There was a Key Error Exception..." + KE)
  except Exception as E:
    print("There was an error... " + E)

  return weather_dict