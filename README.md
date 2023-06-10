# Hangman Game

This is a simple command-line based Hangman game written in Python. The game has three difficulty levels to choose from: `simple`, `intermediate`, and `advanced`.

## How to Play

1. Run the game from your terminal.
2. Choose a difficulty level (`simple`, `intermediate`, or `advanced`).
3. You'll see a series of underscores (_) representing the hidden word.
4. Guess a letter.
5. If your guess is correct, the letter(s) will appear in the word. If your guess is incorrect, part of the hangman will be drawn.
6. Continue guessing letters until you've either guessed the word or the hangman is completely drawn.
7. After the game ends, you'll be prompted to play again or quit the game.

## Prerequisites

- Python 3.6 or above

## How to Run

- Clone the repository
- Navigate to the folder containing the game script
- Run the script in the terminal using python

```bash
python hangman.py
```

## Project Structure

The project contains a `Hangman` class with several methods:

- `__init__`: initializes a new game with the given difficulty.
- `get_status`: checks the game status (won, lost, or in progress).
- `display`: displays the current hangman drawing, guessed letters, and wrong guesses.
- `get_guess`: prompts the user for a guess and validates it.
- `log_guess`: logs the user's guess and updates the game's state.
- `reveal_word`: reveals the word at the end of the game.

---

Have fun :)
