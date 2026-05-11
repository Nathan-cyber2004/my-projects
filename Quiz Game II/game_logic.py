import random
import json

class GameLogic:
  STORED_QUESTIONS = "stored_questions.json"

  def __init__(self):
   # Geography and Landmarks
    self.geography_questions, self.geography_choices, self.geography_answers = self.organize_data()[0]

    # History and Heroes
    self.history_questions, self.history_choices, self.history_answers = self.organize_data()[1]

    # Science and Inventions
    self.science_questions, self.science_choices, self.science_answers = self.organize_data()[2]

    # Language and Literature
    self.language_questions, self.language_choices, self.language_answers = self.organize_data()[3]

    # Pop Culture and Media
    self.culture_questions, self.culture_choices, self.culture_answers = self.organize_data()[4]

    # Nature and Wildlife
    self.nature_questions, self.nature_choices, self.nature_answers = self.organize_data()[5]

    # Space and Astronomy
    self.space_questions, self.space_choices, self.space_answers = self.organize_data()[6]

    # Riddles and Logic Puzzles
    self.riddles_questions, self.riddles_choices, self.riddles_answers = self.organize_data()[7]

    # Random Fun Facts
    self.fun_facts_questions, self.fun_facts_choices, self.fun_facts_answers = self.organize_data()[8]
   
  def ask_question(self):
    pass
  
    
  def get_questions(self, category_name):
    with open(self.__class__.STORED_QUESTIONS, "r") as file:
      data = json.load(file)
    
    list_name = data[category_name]
    questions = []

    for question in list_name:
      questions.append(question["Q"])
    return questions
  
  def get_answers(self, category_name):
    with open(self.__class__.STORED_QUESTIONS, "r") as file:
      data = json.load(file)
    
    list_name = data[category_name]
    answers = []

    for question in list_name:
      answers.append(question["A"])
    return answers
  
  def get_correct_answers(self, category_name):
    with open(self.__class__.STORED_QUESTIONS, "r") as file:
      data = json.load(file)
    
    list_name = data[category_name]
    correct_answers = []

    for question in list_name:
      correct_answers.append(question["Correct"])
    return correct_answers

  def organize_data(self):
    # Geography and Landmarks
    geography_questions = self.get_questions("Geography and Landmarks")
    geography_answers = self.get_answers("Geography and Landmarks")
    geography_correct_answers = self.get_correct_answers("Geography and Landmarks")

    # Geography and Landmarks
    geography_questions = self.get_questions("Geography and Landmarks")
    geography_answers = self.get_answers("Geography and Landmarks")
    geography_correct_answers = self.get_correct_answers("Geography and Landmarks")

    # History and Heroes
    history_questions = self.get_questions("History and Heroes")
    history_answers = self.get_answers("History and Heroes")
    history_correct_answers = self.get_correct_answers("History and Heroes")

    # Science and Inventions
    science_questions = self.get_questions("Science and Inventions")
    science_answers = self.get_answers("Science and Inventions")
    science_correct_answers = self.get_correct_answers("Science and Inventions")

    # Language and Literature
    language_questions = self.get_questions("Language and Literature")
    language_answers = self.get_answers("Language and Literature")
    language_correct_answers = self.get_correct_answers("Language and Literature")

    # Pop Culture and Media
    culture_questions = self.get_questions("Pop Culture and Media")
    culture_answers = self.get_answers("Pop Culture and Media")
    culture_correct_answers = self.get_correct_answers("Pop Culture and Media")

    # Nature and Wildlife
    nature_questions = self.get_questions("Nature and Wildlife")
    nature_answers = self.get_answers("Nature and Wildlife")
    nature_correct_answers = self.get_correct_answers("Nature and Wildlife")

    # Space and Astronomy
    space_questions = self.get_questions("Space and Astronomy")
    space_answers = self.get_answers("Space and Astronomy")
    space_correct_answers = self.get_correct_answers("Space and Astronomy")

    # Riddles and Logic Puzzles
    riddles_questions = self.get_questions("Riddles and Logic Puzzles")
    riddles_answers = self.get_answers("Riddles and Logic Puzzles")
    riddles_correct_answers = self.get_correct_answers("Riddles and Logic Puzzles")

    # Random Fun Facts
    fun_facts_questions = self.get_questions("Random Fun Facts")
    fun_facts_answers = self.get_answers("Random Fun Facts")
    fun_facts_correct_answers = self.get_correct_answers("Random Fun Facts")

    return (
        (geography_questions, geography_answers, geography_correct_answers),
        (history_questions, history_answers, history_correct_answers),
        (science_questions, science_answers, science_correct_answers),
        (language_questions, language_answers, language_correct_answers),
        (culture_questions, culture_answers, culture_correct_answers),
        (nature_questions, nature_answers, nature_correct_answers),
        (space_questions, space_answers, space_correct_answers),
        (riddles_questions, riddles_answers, riddles_correct_answers),
        (fun_facts_questions, fun_facts_answers, fun_facts_correct_answers)
    )

  def get_question_answer(self, questions, correct_answers, answers):
    question = random.choice(questions)
    index_position = questions.index(question)
    answer = answers[index_position]
    correct_answer = correct_answers[index_position]
    return question, correct_answer, answer

game_logic = GameLogic()