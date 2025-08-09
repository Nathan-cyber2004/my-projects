# This file contains the main code logic for the AI Agent

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from art import logo
from get_weather_data import weather_data
from to_do import (add_task, remove_task, view_tasks)
from send_messages import (send_email, send_sms)
from file_handling import summarize_file
from timer import countdown
from news_summarizer import get_news

load_dotenv()

def main():
  # Initialize the model
  model = ChatOpenAI(temperature = 0)
  tools = [weather_data, 
           add_task, 
           remove_task, 
           view_tasks, 
           send_email, 
           send_sms,
           summarize_file,
           countdown,
           get_news]
  
  agent_model = create_react_agent(model, tools)
  chat_history = []

  print(logo)
  print("Hello, I am your personal AI agent! How may I help you?")
  print("Type 'quit' to exit the program...")

  # Continuously get user input
  while True:
    user_input = input("\nYou: ")

    if user_input == "quit":
      print("Have a great day!")
      break

    chat_history.append(HumanMessage(content = user_input))

    for elem in agent_model.stream({"messages": chat_history}):
      if "agent" in elem and "messages" in elem["agent"]:
        for message in elem["agent"]["messages"]:
          print(f"AI Agent: {message.content}", end = "")
          chat_history.append(message.content)
    
    print("") # Newline