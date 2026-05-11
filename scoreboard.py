from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0

    with open("C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Snake Game/data.txt") as data_file:
      self.high_score = int(data_file.read())

    self.color('white')
    self.penup()
    self.goto(0, 260)
    self.hideturtle()
    self.update_board()
  
  def increase_score(self):
    self.score += 1
    self.update_board()
  
  def update_board(self):
    self.clear()
    self.write(f'Score: {self.score}  High Score: {self.high_score}', align = ALIGNMENT, font = FONT)
  
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Snake Game/data.txt", mode = 'w') as data_file:
        data_file.write('{}'.format(self.high_score))
    self.score = 0
    self.update_board()

  
  # def game_over(self):
  #   self.clear()
  #   self.write(f'Game Over', align = ALIGNMENT, font = FONT)
    
