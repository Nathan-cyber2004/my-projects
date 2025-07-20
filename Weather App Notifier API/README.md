#  Weather Notification Program

This is a Python-based weather notification program that fetches current weather data using the OpenWeatherMap API and sends it to the user via email. It also saves the response in a JSON file for easier readability.

---

##  What This Project Does

- Retrieves live weather data using the OpenWeatherMap API
- Parses and filters key weather metrics (temperature, humidity, wind speed, etc.)
- Sends a nicely formatted weather update to your email inbox
- Saves full raw data in `data.json` for transparency and debugging
- Runs daily in the cloud using **PythonAnywhere**

---

##  Technologies Used

- Python 3
- [`requests`](https://pypi.org/project/requests/) – for API calls
- [`smtplib`](https://docs.python.org/3/library/smtplib.html) – to send emails
- [`email.mime`](https://docs.python.org/3/library/email.mime.html) – for formatting email content
- [`dotenv`](https://pypi.org/project/python-dotenv/) – for managing environment variables
- **PythonAnywhere** – to run the script on a daily schedule

---

## Files
weather-notifier/
├── get_data.py # Fetches and filters weather data
├── send_data.py # Sends the filtered data via email
├── main.py # Entry point for execution
├── data.json # Stores last fetched raw weather data

## ✅ How to Run
This script runs automatically via [PythonAnywhere](https://www.pythonanywhere.com/) as a scheduled task so create a free account there and then upload the files.

# Run the script locally with
python main.py
