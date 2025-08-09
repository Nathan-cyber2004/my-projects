import time
import threading
from langchain.tools import tool

@tool
def countdown(user_time: int):
  """This allows the user to set a timer
     Can be expanded on to perform a task after a specific amount of time has passed
  """

  def run_timer():
    for _ in range(user_time, 0, -1):
        time.sleep(1)
    print("Time's Up!")

  # Launch the timer in a new thread
  thread = threading.Thread(target=run_timer, daemon=True)
  thread.start()
  return f"Countdown for {user_time} seconds started in the background."