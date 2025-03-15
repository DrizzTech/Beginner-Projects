import random


def play_game():
    choices = ["rock", "paper", "scissors"]

    # Get user's choice

    print("Welcome to Rock Paper Scissors! Goodluck and have fun playing!")

    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

    # Get computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")


# Play the game
play_game()
