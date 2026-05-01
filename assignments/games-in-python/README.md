
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game using Python strings, loops, conditionals, and user input. Practice program flow, input validation, and game state tracking.

## 📝 Tasks

### 🛠️ Build the Hangman game

#### Description

Write a Python program that randomly selects a secret word and lets the player guess letters until the word is revealed or they run out of attempts.

#### Requirements
Completed program should:

- Choose a secret word from a predefined list.
- Ask the player to guess one letter at a time.
- Display the current word state with underscores for unknown letters.
- Track letters that have already been guessed.
- Reduce remaining attempts only for incorrect guesses.
- End the game with a win or lose message.

### 🛠️ Add player feedback and game polish

#### Description

Improve the game experience by giving clear feedback after each guess and showing the current game status.

#### Requirements
Completed program should:

- Show the player which letters have already been guessed.
- Tell the player whether their guess was correct or incorrect.
- Display the number of remaining attempts.
- Display a final message like `Congratulations, you won!` or `Game over. The correct word was [word].`
- Example interaction:
  ```text
  Word: _ A _ G _ A _
  Guess a letter: N
  Nice! The letter N is in the word.
  Word: _ A N G _ A _
  ```
