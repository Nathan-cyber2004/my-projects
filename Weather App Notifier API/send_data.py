import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from get_data import relevant_data

def send_msg():
    subject = f"Weather Update for {relevant_data[0]}"
    information = (
        f"Temperature: {relevant_data[1]}°F\n"
        f"Feels like: {relevant_data[2]}°F\n"
        f"Minimum Temperature: {relevant_data[3]}°F\n"
        f"Maximum Temperature: {relevant_data[4]}°F\n"
        f"Description: {relevant_data[5]}\n"
        f"Humidity: {relevant_data[6]}%\n"
        f"Wind Speed: {relevant_data[7]} mph"
    )

    username = "EMAIL ADDRESS"
    password = "GOOGLE APP PASSWORD"

    # mime allows for the fahrenheit symbol to be used when sending email
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = username
    msg["Subject"] = subject
    msg.attach(MIMEText(information, "plain", "utf-8"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, username, msg.as_string())
        print("Message sent successfully!")
    except Exception as e:
        print(f"Email failed: {e}")
