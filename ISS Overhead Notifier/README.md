# 🛰️ ISS Notifier

A Python script that notifies you via email when the **International Space Station (ISS)** is currently passing near your location **and** it’s dark enough to see it overhead.

---

## Features

- Fetches the **current position of the ISS** using the [Open Notify API](http://api.open-notify.org/iss-now.json).
- Uses the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine local daylight hours.
- Checks your location’s latitude and longitude to see if the ISS is nearby.
- Sends an **email notification** if:
  - The ISS is within ±10° of your location, and  
  - It is currently **nighttime**.
- Runs continuously, checking every 60 seconds.

---

## How It Works

1. **Get ISS Coordinates**  
   The script calls `http://api.open-notify.org/iss-now.json` to get the ISS’s current latitude and longitude.

2. **Check Proximity**  
   If the ISS’s coordinates are within ±10 degrees of your location, it’s considered “overhead.”

3. **Get Sunrise/Sunset Times**  
   Uses the [Sunrise-Sunset API](https://api.sunrise-sunset.org/json) to find sunrise and sunset times for your latitude and longitude.

4. **Check Time of Day**  
   If it’s dark (before sunrise or after sunset), proceed to send the notification.

5. **Send Email**  
   Sends an email with the subject **"Look Up!"** to notify you that the ISS is visible.

---

## Requirements

- Python 3.8+
- Internet connection (for API calls)
- Access to an SMTP email account (like Gmail)

### Python Libraries

Install dependencies with:

```bash
pip install requests
