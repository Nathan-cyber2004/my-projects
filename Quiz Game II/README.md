# Brain Blitz Quiz Game

Brain Blitz is a Python-based trivia quiz game with a graphical user interface. Players can choose from multiple knowledge categories and answer multiple-choice questions in a lightweight desktop app.

## Features

- Category-based quiz play
- Multiple-choice questions with instant feedback
- GUI built with `tkinter`
- Question data loaded from a local JSON file
- Includes categories like Geography, History, Science, Literature, Pop Culture, Nature, Space, Riddles, and Fun Facts

## Project Structure

- `main.py` - Application entry point that launches the GUI
- `ui.py` - Graphical user interface and quiz interaction logic
- `game_logic.py` - Question loading and answer selection logic
- `get_questions.py` - Category-specific helper functions for selecting and removing questions
- `create_questions.py` - Web scraping helper script to extract question data from a trivia site
- `stored_questions.json` - Local question database used by the game
- `quiz_game_icon.png`, `OIP.png` - Image assets used by the interface

## Requirements

- Python 3.8+
- `tkinter` (usually included with Python)
- `Pillow` for image support

Optional (only if you want to use `create_questions.py`):
- `selenium`
- Microsoft Edge WebDriver (`msedgedriver.exe`)

## Installation

1. Install Python 3.8 or newer.
2. Install dependencies:

```bash
pip install pillow
```

If you plan to run the question scraper:

```bash
pip install selenium
```

## Running the Quiz Game

Start the game by running:

```bash
python main.py
```

This will launch the Brain Blitz GUI, where you can select a category and answer trivia questions.

## Notes

- `stored_questions.json` contains the quiz questions, answer choices, and correct answers.
- The helper script `create_questions.py` is intended to populate or update `stored_questions.json`, but it requires a working Selenium environment and the Edge WebDriver.
- The current game flow selects a random question from the chosen category and removes it from that category for the current session.

## Improvements

Potential future enhancements:

- Add score tracking and session summaries
- Add a timed quiz mode
- Improve question reloading so categories reset automatically after completion
- Add more question categories and better error handling

## License

This project is provided as-is for personal or demonstration use.
