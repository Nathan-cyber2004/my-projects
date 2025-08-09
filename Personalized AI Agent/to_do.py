# This file contains the logic for getting and storing tasks as well as removing them

import os
from langchain.tools import tool

@tool
def add_task(designated_task, file_name = "all_tasks.txt"):
  """This function adds a task to a json file for future reference"""
  if os.path.exists(file_name):
    with open(file_name, "a") as file:
      file.write("\n" + designated_task)
  else:
    with open("all_tasks.txt", "w") as new_file:
      new_file.write(designated_task)

@tool
def remove_task(designated_task, file_name = "all_tasks.txt"):
    """Removes a task from the text file by matching text (case-insensitive)."""
    if not os.path.exists(file_name):
        return "No task file found."

    with open(file_name, "r") as file:
        notes = file.readlines()

    with open(file_name, "w") as file:
        for note in notes:
            if note.strip().lower() != designated_task.strip().lower():
                file.write(note)

@tool
def view_tasks(file_name = "all_tasks.txt"):
   """This function returns all the tasks that the user has stored"""
   with open(file_name, "r") as read_file:
      all_tasks = read_file.readlines()
   return all_tasks