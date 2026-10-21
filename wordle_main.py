from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won
)

def play_game():
    #Play one round of wordle
    secret_word = choose_word()
    previous_guesses = []
    max_attempts = 6

    print("Welcome to Python Wordle!")
    print("Guess the secret five-letter word.")
    print("G = correct letter and position")
    print("Y = letter is in the word, but in the wrong position")
    print("- = letter is not in the word")
    print("You have six attempts.")

    # Continue until the player wins or runs out of attempts.
    while len(previous_guesses) < max_attempts:
        print("Attempt", len(previous_guesses) + 1, "of", max_attempts)

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("Congratulations! You guessed the word!")
            return

        print()

    # Reveal the secret word if the player loses.
    print("Game over! The secret word was:", secret_word)


# Ask whether the player wants another round.
play_again = "yes"

while play_again == "yes" or play_again == "y":
    play_game()
    play_again = input(
        "Would you like to play again? (YES/NO): "
    ).upper()

print("Thanks for playing!")
