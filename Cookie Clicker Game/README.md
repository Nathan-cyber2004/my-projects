## Cookie Clicker Automation (Selenium)

This Python script automates gameplay for the popular browser game Cookie Clicker
using Selenium and the Microsoft Edge WebDriver.
It automatically clicks the main cookie and purchases available upgrades to increase cookie production over time.

# Features

Automatically launches Cookie Clicker in Microsoft Edge.

Repeatedly clicks the main cookie to generate cookies.

Monitors the current cookie count in real time.

Buys upgrades whenever enough cookies are available.

Runs continuously until manually stopped.

# Requirements

Python 3.8+

Selenium (pip install selenium)

Microsoft Edge WebDriver (msedgedriver.exe) — must match your Edge browser version.

# Setup & Usage

Install dependencies:

pip install selenium


Download Microsoft Edge WebDriver:

Go to Microsoft Edge Developer

Download the version that matches your Edge browser.

Place msedgedriver.exe in the same folder as this script.

Run the script:

python cookie_clicker_bot.py


The bot will:

Open Cookie Clicker.

Automatically select English as the language.

Continuously click the cookie.

Purchase upgrades when possible.

# Stopping the Bot

Press Ctrl + C in the terminal or close the browser window to stop the script.

# Notes

This script is for educational purposes only — use responsibly.

Avoid overloading the game servers with excessive automation.

You can modify the for i in range(4): loop to check more upgrade slots.
