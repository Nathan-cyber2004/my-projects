from turtle import Turtle

POSITIONS = [(0,0), (-20,0), (-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):
    self.snake_body = []
    self.create_snake()
    self.snake_head = self.snake_body[0]

  def create_snake(self):
    for position in POSITIONS:
      self.add_segment(position)
      
  def add_segment(self, position):
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    self.snake_body.append(new_segment)

  def extend(self):
    self.add_segment(self.snake_body[-1].position())
  
  def reset(self):
    for seg in self.snake_body:
      seg.goto(1000, 1000)
    self.snake_body.clear()
    self.create_snake()
    self.snake_head = self.snake_body[0]

  def move(self):
    for segment in range(len(self.snake_body) - 1, 0, -1):
      new_x = self.snake_body[segment - 1].xcor()
      new_y = self.snake_body[segment - 1].ycor()
      self.snake_body[segment].goto(new_x, new_y)
    
    self.snake_body[0].forward(20)
  
  def move_up(self):
    if self.snake_head.heading() != DOWN:
      self.snake_head.setheading(UP)

  def move_down(self):
    if self.snake_head.heading() != UP:
      self.snake_head.setheading(DOWN)

  def move_left(self):
    if self.snake_head.heading() != RIGHT:
      self.snake_head.setheading(LEFT)

  def move_right(self):
    if self.snake_head.heading() != LEFT:
      self.snake_head.setheading(RIGHT)