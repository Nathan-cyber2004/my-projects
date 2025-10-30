import requests
import datetime as dt
import smtplib
import time

# Constants

MY_LAT = 35.779591
MY_LNG = -78.638176

MY_EMAIL = 'nathanpereira204@gmail.com'
MY_PASSWORD = '12106810'


# ISS_Positions

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])


def is_iss_overhead():
  '''Function to determine whether the ISS is close to us'''
  distance_lat = abs(MY_LAT - latitude)
  distance_lng = abs(MY_LNG - longitude)

  if distance_lat <= 10 and distance_lng <= 10:
    return True
  else:
    return False


# Sunset and Sunrise 

parameters = {
  'lat': MY_LAT,
  'lng': MY_LNG,
  'formatted': 0
}

second_response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
second_response.raise_for_status()
second_data = second_response.json()

sunrise_time_data = second_data['results']['sunrise']
sunset_time_data = second_data['results']['sunset']

sunrise_time = int(sunrise_time_data.split('T')[1].split(':')[0])
sunset_time = int(sunset_time_data.split('T')[1].split(':')[0])


# Current Time

now = dt.datetime.now()
sample_time = str(now)
current_time = int(sample_time.split(' ')[1].split(':')[0])


def is_nightime():
  '''Function to determine whether it is currently dark outside'''
  if current_time < sunrise_time or current_time > sunset_time:
    return True
  else:
    return False
  

# Logic to send email if conditions are met

while True:
  time.sleep(60)  # Run this code every 60 secods

  if is_iss_overhead():
    if is_nightime():
      with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(msg = 'Subject: Look Up!\n\nThe International Space Station is near you!')
  print('Code has successfully been run!')