import random

def play_game():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    if player_choice not in options:
        print("Invalid choice, please try again.")
        return play_game()
    print("Computer chose: ", computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")

play_game()

