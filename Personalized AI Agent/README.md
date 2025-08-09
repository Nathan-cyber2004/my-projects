# Personalized AI Agent

## Overview

This project is a versatile **AI Agent** built using LangChain and OpenAI’s API. It supports multiple functionalities such as:

- Conversational AI with memory of prior messages
- Weather information retrieval
- Task management (add, remove, view tasks)
- Sending emails and SMS messages
- File reading and summarization 
- Timer functionality 

---

## Features

- **Conversational AI:** Chat naturally with memory of past interactions.
- **Weather Tool:** Get current weather data by location.
- **Task Manager Tool:** Add, remove, and view tasks stored in a file.
- **Messaging Tool:** Send emails or SMS messages using integrated tools.
- **News Tool:** Scrapes a website for the news (For educational use, non-commercial)
- **Extensible:** Easily add new tools or functionalities.

---

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API Key
- Weather API Key (OpenWeatherMap)
- Email and SMS credentials for messaging (optional)
- pip or uv package manager

### Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/ai-agent.git
   cd ai-agent
   
2. Create a virtual environment

- python -m venv .venv
- .venv/bin/activate   # macOS/Linux
- .venv\Scripts\activate      # Windows

3. Install dependencies (I used uv for this project)
- pip install uv -> To install uv
- uv add dependency -> To install dependencies using uv

4. Add API Keys to a .env file
- OPENAI_API_KEY=your_openai_api_key
- WEATHER_API_KEY=your_weather_api_key
- EMAIL_USERNAME=your_email@example.com
- EMAIL_PASSWORD=your_email_password
