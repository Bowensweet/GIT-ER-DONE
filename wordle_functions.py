import random

# A list of five-letter words the game can choose from.
words = ["plant", "crane", "brick", "shout", "flame",
         "ghost", "trail", "mouse", "bread", "cloud"]


def choose_word():
    """Select and return a random secret word."""
    return random.choice(words)


def get_guess(previous_guesses):
    while True:
        guess = input("Enter a five-letter word: ").upper()

        # Check whether every character is a letter.
        valid_guess = True

        for letter in guess:
            if letter < "A" or letter > "Z":
                valid_guess = False

        # Check the length and whether the guess contains only letters.
        if len(guess) != 5 or not valid_guess:
            print("Your guess must contain exactly five letters.")

        # Make sure the player has not used this guess already.
        elif guess in previous_guesses:
            print("You already guessed that word. Try another.")

        else:
            return guess


def evaluate_guess(guess, secret_word):
    #Return G, Y, or - for each letter.
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
    #Display the guess and its feedback.
    print("Guess:    " + " ".join(guess))
    print("Feedback: " + " ".join(feedback))


def has_won(guess, secret_word):
    #Check whether the player guessed the secret word.
    return guess == secret_word
