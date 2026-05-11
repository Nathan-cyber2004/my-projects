# Snake Game

A classic Snake game built with Python's built-in `turtle` graphics module.

Guide the snake around the screen, eat the red food, and try to beat the saved high score. The snake grows each time it eats food. If it hits the wall or its own tail, the current score resets and the game starts over.

## Features

- Arrow-key snake movement
- Randomly spawning food
- Growing snake body
- Wall and tail collision detection
- Persistent high score saved in `data.txt`

## Project Files

```text
Snake Game/
|-- main.py          # Starts the game and runs the main game loop
|-- snake.py         # Snake movement, growth, and reset behavior
|-- food.py          # Food appearance and random placement
|-- scoreboard.py    # Score display and high score saving
`-- data.txt         # Saved high score
```

## Requirements

- Python 3.x

No third-party packages are required. The game uses Python's standard `turtle` module.

## How to Run

From this project folder, run:

```bash
python main.py
```

Use the arrow keys to control the snake:

- `Up` moves up
- `Down` moves down
- `Left` moves left
- `Right` moves right

## High Score Note

The high score is stored in `data.txt`. In the current version, `scoreboard.py` uses an absolute path to read and write that file:

```python
C:/Users/Nathan/Desktop/The Complete Guide to Python/Angela Yu Python Programming/Python Projects/Snake Game/data.txt
```

If you move this project to a different folder or computer, update that path or change it to a relative path such as:

```python
with open("data.txt") as data_file:
```

and:

```python
with open("data.txt", mode="w") as data_file:
```

## Credits

Created as part of the Python learning projects from Angela Yu's course.
