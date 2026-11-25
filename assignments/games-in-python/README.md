
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a complete Hangman game using Python strings, loops, conditionals, random selection, and user input. You will practice translating game rules into clear program logic and creating an interactive experience for the player.

## 📝 Tasks

### 🛠️ Set Up the Word Selection

#### Description
Create the starting data and functions for a Hangman game.

#### Requirements
Completed program should:

- Store at least 10 words in a predefined list.
- Randomly select one word for each game.
- Convert the selected word to lowercase.
- Display the word's length using underscores, such as `_ _ _ _`.

### 🛠️ Process Player Guesses

#### Description
Implement the main game loop so the player can repeatedly enter letter guesses.

#### Requirements
Completed program should:

- Prompt the player to enter one letter at a time.
- Accept letters regardless of whether they are entered in uppercase or lowercase.
- Reveal every matching letter in the displayed progress.
- Track each incorrect guess and display the number of attempts remaining.
- Avoid reducing attempts for a repeated guess that is already in the guess history.
- Continue until the player wins or runs out of attempts.

### 🛠️ Complete the Game Flow

#### Description
Add clear win and lose outcomes and make the game ready to play again.

#### Requirements
Completed program should:

- Display a win message when every letter in the word has been guessed.
- Display a lose message and reveal the hidden word when the attempts reach zero.
- Ask the player whether they want to play again.
- Start a new game with another randomly selected word when the player chooses to continue.
