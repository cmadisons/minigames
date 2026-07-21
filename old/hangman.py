"""
Hangman — a small word-guessing game.

The player guesses one letter at a time. A wrong guess costs a life.
Reveal the whole word before running out of lives to win.

Just play it: type letters and read what it prints back. Every bug in here
can be found by giving inputs and checking the output against what you'd expect.
"""

import random

# WORDS = ["python", "boolean", "iterator"]
WORDS = ["boolean"]
MAX_LIVES = 5


def choose_word(words=WORDS):
    """Pick a random secret word."""
    return random.choice(words)


def mask_word(word, guessed):
    """Show guessed letters; hide the rest as underscores."""
    shown = [c if c in guessed else "_" for c in word]
    return " ".join(shown)


def is_won(word, guessed):
    """True when the word has been fully revealed."""
    return all(c in guessed for c in word)


def get_guess():
    """Prompt until the player types a single letter."""
    while True:
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue
        return letter


def play():
    word = choose_word()
    guessed = []
    wrong = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_LIVES} lives.\n")

    while wrong < MAX_LIVES:
        print(mask_word(word, guessed))
        print(f"Lives left: {MAX_LIVES - wrong}")

        letter = get_guess()
        if letter in guessed:
            print(f"You already guessed '{letter}'. Try another.\n")
            continue
        guessed.append(letter)

        if letter in word:
            print(f"Good guess! '{letter}' is in the word.\n")
        else:
            wrong += 1
            print(f"Sorry, '{letter}' is not in the word.\n")

        if is_won(word, guessed):
            print(f"You won! The word was '{word}'.")
            return

    print(f"Out of lives! The word was '{word}'.")


if __name__ == "__main__":
    play()
