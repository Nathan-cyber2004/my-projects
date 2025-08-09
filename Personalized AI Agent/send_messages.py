# This file contains the code logic for sending emails and SMS messages

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Uses mime for adding potential symbols

@tool
def send_email(to_email, desired_text):
  """Allows for emails to be sent"""
  try:
    msg = MIMEMultipart()
    msg["From"] = MY_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "A message from Nathan's AI Agent" # Personalize to whatever you want
    msg.attach(MIMEText(desired_text, "plain", "utf-8"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(MY_EMAIL, PASSWORD)
    server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
    print("Message sent successfully!")
  except Exception as E:
    print("There was an error... " + str(E))
  finally:
    server.quit()

@tool
def send_sms(to_number, desired_text):
  """Allows for text messages to be sent"""
  try:
    msg = EmailMessage()
    msg.set_content(desired_text)

    msg['From'] = MY_EMAIL # 'email@address.com'
    msg['To'] = f"{to_number}@vtext.com"  # '1112223333@vmobl.com' -> Depending on user, might need to change email to SMS domain
    msg['Subject'] = "A message from Nathan's AI Agent"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_EMAIL, PASSWORD)

    server.send_message(msg)
  except Exception as E:
    print("There was an error... " + str(E))
  finally:
    server.quit()