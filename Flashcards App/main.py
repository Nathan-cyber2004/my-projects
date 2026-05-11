import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD = "C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Flashcards App/images/card_front.png"
BACK_CARD = "C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Flashcards App/images/card_back.png"
RIGHT = "C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Flashcards App/images/right.png"
WRONG = "C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Flashcards App/images/wrong.png"
FRENCH_WORDS = "C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Flashcards App/data/french_words.csv"
PATH_TO_WORDS = "C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Flashcards App/words_to_learn.csv"

# Obtaining data
current_card = {}
to_learn = {}

try:
  data = pandas.read_csv(PATH_TO_WORDS)
except:
  original_data = pandas.read_csv(FRENCH_WORDS)
  to_learn = original_data.to_dict(orient = 'records')
else:  
  to_learn = data.to_dict(orient = 'records')


# Function to display next card
def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  french_word = current_card['French']
  canvas.itemconfig(card_title, text = 'French', fill = 'black')
  canvas.itemconfig(card_word, text = french_word, fill = 'black')
  canvas.itemconfig(card_background, image = card_front_img)
  flip_timer = window.after(3000, func = flip_card)

# Function to flip card
def flip_card():
  canvas.itemconfig(card_title, text = 'English', fill = 'white')
  canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')
  canvas.itemconfig(card_background, image = card_back_img)

def is_known():
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  data.to_csv(PATH_TO_WORDS, index = False)

  next_card()

# Initializing window
window = Tk()
window.title('Flashy')
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

# Initializing canvas
canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file = FRONT_CARD)
card_back_img = PhotoImage(file = BACK_CARD)
card_background = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150, text = 'Title', font = ('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text = 'word', font = ('Arial', 60, 'bold'))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row = 0, column = 0, columnspan = 2)


# Initializing buttons
right_img = PhotoImage(file = RIGHT)
right_button = Button(image = right_img, command = is_known)
right_button.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
right_button.grid(column = 1, row = 1)

wrong_img = PhotoImage(file = WRONG)
wrong_button = Button(image = wrong_img, command = next_card)
wrong_button.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
wrong_button.grid(column = 0, row = 1,)


next_card()


window.mainloop()