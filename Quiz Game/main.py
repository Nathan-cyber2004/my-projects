from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quiz_bank = []

for num in range(len(question_data)):
  text = question_data[num]['text']
  answer = question_data[num]['answer']
  quiz_bank.append(Question(text, answer))

quiz_brain = QuizBrain(quiz_bank)


while quiz_brain.still_has_questions():
  quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
