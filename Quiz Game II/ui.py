from tkinter import *
from get_questions import *
from PIL import Image, ImageTk

class GUI:
    WINDOW_SIZE = "960x485"
    BACKGROUND_COLOR = "#121212"

    def __init__(self):
        self.root = Tk()
        self.root.title("Brain Blitz")
        self.root.geometry(self.__class__.WINDOW_SIZE)
        self.root.config(background=self.__class__.BACKGROUND_COLOR)
        self.icon_image = ImageTk.PhotoImage(Image.open("quiz_game_icon.png"))  # Convert to Tk format
        self.root.iconphoto(True, self.icon_image)
        self.main_menu()

    def main_menu(self):
        self.clear_window()  # Ensure the window is cleared before adding new widgets

        # Create Labels
        self.welcome = Label(self.root, text="Brain Blitz", font=("Georgia", 25, "bold"), fg="#E0E0E0", bg=self.__class__.BACKGROUND_COLOR)
        self.welcome.grid(row=0, column=1, padx=5, pady=5)

        # Category Buttons
        categories = [
            ("Geography and Landmarks", get_geography_question, "#32CD32"),
            ("History and Heroes", get_history_question, "#FFFF00"),
            ("Science and Inventions", get_science_question, "#1E90FF"),
            ("Language and Literature", get_language_question, "#FF4500"),
            ("Pop Culture and Media", get_culture_question, "#FF6347"),
            ("Nature and Wildlife", get_nature_question, "#800080"),
            ("Space and Astronomy", get_space_question, "#32CD32"),
            ("Riddles and Logic", get_riddle_question, "#40E0D0"),
            ("Random Fun Facts and Trivia", get_fun_facts_question, "#FF7F50"),
        ]
        try:
          for index, (text, func, color) in enumerate(categories):
              if func == False:
                  self.display_no_questions()
              else:
                  row, col = divmod(index, 3)  # Arrange buttons in a grid
                  button = Button(self.root, text=text, font=("Georgia", 15), bg=color, width=25,
                                  command=lambda f=func: self.ask_question(f))
                  button.grid(row=row + 1, column=col, padx=5, pady=5)
        except Exception as E:
            print("There was an error", E)
            self.display_no_questions()

        # Logo Image
        self.image = ImageTk.PhotoImage(Image.open("OIP.png"))
        self.my_image_label = Label(self.root, image=self.image, bg=self.__class__.BACKGROUND_COLOR)
        self.my_image_label.grid(row=4, column=1, pady=10)

        self.root.mainloop()

    def ask_question(self, func_name):
      self.clear_window()

      # Let's assume this function returns 3 values (question, answer, options)
      result = func_name()  # E.g., result = ('What is 2+2?', '4', ['2', '3', '4', '5'])

      question = result[0]
      options = result[1]
      answer = result[2] 

      
      self.question_label = Label(self.root, text=question, font=("Georgia", 18), fg="white", bg=self.__class__.BACKGROUND_COLOR)
      self.question_label.pack(pady=20)

      # Code to display buttons
      for option in options:
          option_button = Button(self.root, text=option, font=("Georgia", 15), bg="#FF4500", width=15,
                                command=lambda opt=option: self.check_answer(opt, answer))
          option_button.pack(pady=5)

    def check_answer(self, user_input, correct_answer):

        self.clear_window()

        if user_input == correct_answer:
            result_text = "Correct!"
            color = "#32CD32"  # Green
        else:
            result_text = f"Incorrect! The correct answer was: {correct_answer}"
            color = "#FF4500"  # Red

        result_label = Label(self.root, text=result_text, font=("Georgia", 18), fg=color, bg=self.__class__.BACKGROUND_COLOR, width=50)
        result_label.pack(pady=20)

        return_button = Button(self.root, text="Back to Menu", font=("Georgia", 15), bg="#FFFF00", width=15, command=self.main_menu)
        return_button.pack(pady=10)
    
    def display_no_questions(self):
        self.clear_window()

        zero_questions = "You have completed all the questions in this genre, please continue to the next one..."

        self.no_questions_label = Label(self.root, text = zero_questions, font=("Georgia", 18), fg= "white", bg=self.__class__.BACKGROUND_COLOR, width=50)
        self.no_questions_label.pack(pady = 10)

    def clear_window(self):
        """Removes all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

gui = GUI()