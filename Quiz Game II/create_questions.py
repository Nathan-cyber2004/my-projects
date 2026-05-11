from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import json

class RetrieveQuestions:

  URL = "https://triviamaker.com/fifth-grader-questions/"
  STORED_QUESTIONS = "stored_questions.json"

  def __init__(self):
    self.service = Service(executable_path = "msedgedriver.exe")
    self.driver = webdriver.Edge(service = self.service)
    self.driver.get(self.__class__.URL)
  
  def extract_questions(self):
    # Geography and Landmarks
    geography_and_landmark = self.extract_format(12,32)

    # History and Heroes
    history_and_heores = self.extract_format(33, 53)
  
    # Science and Inventions
    science_and_inventions = self.extract_format(54, 74)
  
    # Language and Literature
    language_and_literature = self.extract_format(75, 95)
  
    # Pop Culture and Media
    pop_culture_and_media = self.extract_format(96, 116)
  
    # Nature and Wildlife
    nature_and_wildlife = self.extract_format(117, 137)
  
    # Space and Astronomy
    space_and_astronomy = self.extract_format(138, 158)
  
    # Riddles and Logic Puzzles
    riddles_and_logic = self.extract_format(159, 179)
  
    # Random Fun Facts
    random_fun_facts = self.extract_format(180, 200)

    # Return each list
    return (geography_and_landmark, 
            history_and_heores, 
            science_and_inventions, 
            language_and_literature, 
            pop_culture_and_media, 
            nature_and_wildlife,
            space_and_astronomy,
            riddles_and_logic,
            random_fun_facts
    )
  
  def save_questions(self):
    new_data = self.extract_questions()

    formatted_data = {
    "Geography and Landmarks": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[0]
    ],
    "History and Heroes": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[1]
    ],
    "Science and Inventions": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[2]
    ],
    "Language and Literature": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[3]
    ],
    "Pop Culture and Media": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[4]
    ],
    "Nature and Wildlife": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[5]
    ],
    "Space and Astronomy": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[6]
    ],
    "Riddles and Logic Puzzles": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[7]
    ],
    "Random Fun Facts": [
        {"Q": question.split("A:")[0].strip(), "A": question.split("A:")[1].strip() if "A:" in question else "Answer not extracted"} 
        for question in new_data[8]
    ],
    }

    try:
      with open(self.__class__.STORED_QUESTIONS, "w") as new_file:
        json.dump(formatted_data, new_file, indent = 4)
    except Exception as E:
      print("There was an error writing to file", E)

      

  def extract_format(self, start_index, end_index):
    quiz_questions = []
    
    questions = self.driver.find_elements(By.TAG_NAME, "p")
    for question in questions[start_index:end_index]:
      text = question.get_attribute("textContent").strip()
      quiz_questions.append(text)
    
    return quiz_questions

retrive_questions = RetrieveQuestions()
retrive_questions.remove_unicode()