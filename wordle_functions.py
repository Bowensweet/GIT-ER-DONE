import random

# A list of five-letter words the game can choose from.
WORDS = ["PLANT", "CRANE", "BRICK", "SHOUT", "FLAME",
         "GHOST", "TRAIL", "MOUSE", "BREAD", "CLOUD"]


def choose_word():
    """Select and return a random secret word."""
    return random.choice(WORDS)


def get_guess(previous_guesses):
    """Get a valid five-letter guess that has not been used."""
    while True:
        guess = input("Enter a five-letter word: ").upper()

        if len(guess) != 5 or not guess.isalpha():
            print("Your guess must contain exactly five letters.")
        elif guess in previous_guesses:
            print("You already guessed that word. Try another.")
        else:
            return guess


def evaluate_guess(guess, secret_word):
    """Return G, Y, or - for each letter."""
    feedback = []

    for position in range(5):
        if guess[position] == secret_word[position]:
            feedback.append("G")
        elif guess[position] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback


def display_guess(guess, feedback):
    """Display the guess and its feedback."""
    print("Guess:    " + " ".join(guess))
    print("Feedback: " + " ".join(feedback))


def has_won(guess, secret_word):
    """Check whether the player guessed the secret word."""
    return guess == secret_word
