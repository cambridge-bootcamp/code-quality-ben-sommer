# Wordle clone to add pytypes to
import random


def select_word(word_list_path):
    """Selects a random 5-letter word from a file."""
    try:
        with open(word_list_path, "r") as f:
            words = [line.strip().upper() for line in f if len(line.strip()) == 5]
            if not words:
                print("Word list is empty or contains no 5-letter words.")
                return "HELLO"
            return random.choice(words)
    except FileNotFoundError:
        print(f"Warning: '{word_list_path}' not found. Using a default word.")
        return "PYTHON"


def check_guess(guess, secret_word):
    """
    Compares the guess against the secret word and returns the result.
    """
    if len(guess) != len(secret_word):
        raise ValueError("Guess must be the same length as the secret word.")

    result = []
    secret_word_counts = {char: secret_word.count(char) for char in secret_word}

    # First pass: check for 'correct' letters
    for i in range(len(guess)):
        char = guess[i]
        if char == secret_word[i]:
            result.append((char, "correct"))
            secret_word_counts[char] -= 1
        else:
            # Placeholder for the second pass
            result.append((char, "wrong"))  # Default to 'wrong'

    # Second pass: check for 'misplaced' letters
    for i in range(len(guess)):
        # Only check letters that aren't already correct
        if result[i][1] == "correct":
            continue

        char = guess[i]
        if char in secret_word_counts and secret_word_counts[char] > 0:
            result[i] = (char, "misplaced")
            secret_word_counts[char] -= 1

    return result


def display_result(result):
    """Displays the colored result of a guess."""
    # ANSI escape codes for colors
    colors = {
        "correct": "\033[92m",  # Green
        "misplaced": "\033[93m",  # Yellow
        "wrong": "\033[90m",  # Grey
        "end": "\033[0m",  # Reset
    }
    output = "  "
    for letter, state in result:
        output += f"{colors[state]}{letter}{colors['end']} "
    print(output)


def play_game():
    """Main function to run the word puzzle game."""
    # Create a dummy word list for the example
    with open("words.txt", "w") as f:
        f.write("HELLO\nABOUT\nTRACK\nSPLAT\nBRAIN\n\n\n")

    secret = select_word("words.txt")
    attempts = 6
    print("--- Welcome to the Word Puzzle ---")
    print(f"Guess the {len(secret)}-letter word. You have {attempts} attempts.")

    for i in range(attempts):
        guess = ""
        while len(guess) != len(secret):
            guess = input(f"\nAttempt {i + 1}/{attempts}: ").upper().strip()
            if len(guess) != len(secret):
                print(f"Please enter a {len(secret)}-letter word.")

        guess_feedback = check_guess(guess, secret)
        display_result(guess_feedback)

        if guess == secret:
            print(f"\nCongratulations! You guessed it: {secret}")
            return

    print(f"\nGame over! The word was: {secret}")


if __name__ == "__main__":
    play_game()
