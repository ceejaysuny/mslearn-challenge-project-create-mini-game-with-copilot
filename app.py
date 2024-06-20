import random

def get_computer_choice():
    """Randomly select between rock, paper, and scissors."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Prompt the user to enter a choice and validate it."""
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    """Play the game of rock, paper, scissors."""
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            print("You won!")
            user_score += 1
        elif result == "lose":
            print("You lost!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score: You {user_score} - Computer {computer_score}")
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()