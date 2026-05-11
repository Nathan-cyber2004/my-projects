import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup
screen = Screen()
screen.title('Snake Game')
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.tracer(0)

# Initializing the snake's body
snake = Snake()

# Initializing apple
food = Food()

# Initializing scoreboard
scoreboard = Scoreboard()

# User's movements
screen.listen()

screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')


playing = True

while playing:
  screen.update()
  time.sleep(0.1)

  # Movement logic
  snake.move()

  # Apple collision
  if snake.snake_head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    snake.extend()

  # Wall collision
  if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285 or snake.snake_head.ycor() > 285 or snake.snake_head.ycor() < -285:
    scoreboard.reset()
    snake.reset()
  
  # Tail collision
  for segment in snake.snake_body[1:]:
    if snake.snake_head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()


screen.exitonclick()