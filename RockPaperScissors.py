import random

choices = ("rock", "paper", "scissors")

# Establish what choice defeats which
victory = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def get_player_choice():
    #Prompt the player, lowercase the response, validate it, and return it.
    while True:
        choice = input("What do you choose? (rock, paper, or scissors): ").lower()
        if choice in choices:
            return choice
        print("Please type rock, paper, or scissors.")


def determine_winner(player, computer):
    #Compare the two choices and return 'win', 'loss', or 'tie' for the player.
    if player == computer:
        return "tie"
    if victory[player] == computer:
        return "win"
    return "loss"


def get_number_of_rounds():
    #Ask for the number of rounds and make sure it is a positive and odd number.
    while True:
        response = input("How many rounds would you like to play? (enter an odd number): ")
        try:
            rounds = int(response)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if rounds < 1:
            print("The number of rounds must be at least 1.")
        elif rounds % 2 == 0:
            print("Please enter an odd number. No ties!")
        else:
            return rounds


def game():
    print()
    print(" Welcome to Rock, Paper, Scissors!")
    print()

    total_rounds = get_number_of_rounds()

    player_wins = player_losses = 0
    computer_wins = computer_losses = 0
    rounds_completed = 0

    # Ties don't count
    while rounds_completed < total_rounds:
        print(f"Round {rounds_completed + 1} of {total_rounds}")
        player_choice = get_player_choice()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("Tie! It doesn't count!")
            continue

        if result == "win":
            print("You win this round!")
            player_wins += 1
            computer_losses += 1
        else:
            print("You lose this round!")
            computer_wins += 1
            player_losses += 1

        rounds_completed += 1
        print(f"Score -> You: {player_wins} | Computer: {computer_wins}")

    # Print results
    print()
    print("  GAME OVER - FINAL RESULTS")
    print()
    print(f"Player - Wins: {player_wins}, Losses: {player_losses}")
    print(f"Computer - Wins: {computer_wins}, Losses: {computer_losses}")

    if player_wins > computer_wins:
        print("Winner, winner, chicken dinner!")
    else:
        print("Better luck next time, loser!")

game()