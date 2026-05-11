# Higher Lower Game

A simple command-line Python game inspired by the classic "Higher or Lower" format.

The game shows two famous people, brands, or organizations and asks you to guess which one has more Instagram followers. Each correct answer increases your score. The game ends when you guess incorrectly.

## How to Run

Make sure Python is installed, then run the game from this project folder:

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
python3 main.py
```

## How to Play

1. The game displays two options: `A` and `B`.
2. Type `A` if you think option A has more followers.
3. Type `B` if you think option B has more followers.
4. If you are correct, your score increases and the game continues.
5. If you are incorrect, the game ends and shows your final score.

## Project Files

- `main.py` - Contains the main game logic.
- `game_data.py` - Stores the list of accounts, follower counts, descriptions, and countries.
- `art.py` - Stores the ASCII art logo and versus graphic.

## Notes

- Follower counts are stored in millions.
- The game uses the local data in `game_data.py`, so the follower counts may not match current real-world numbers.
- No external Python packages are required.

## Possible Improvements

- Prevent repeated comparisons from appearing too often.
- Validate user input when something other than `A` or `B` is entered.
- Display the final score with a clearer game-over message.
