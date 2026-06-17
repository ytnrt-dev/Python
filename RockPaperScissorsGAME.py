import random

options = ["rock", "paper", "scissors"]

while True:
    player_score   = 0
    computer_score = 0

    print("\n=== Rock, Paper, Scissors ===")
    print("First to 3 wins!")

    while player_score < 3 and computer_score < 3:
        print(f"\nScore  -  You: {player_score}  |  Computer: {computer_score}")
        player = input("Enter your choice (rock, paper, scissors): ").strip().lower()

        if player not in options:
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(options)
        print(f"\nComputer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock"     and computer == "scissors"):
            print(f"You win this round!")
            player_score += 1
        elif (player == "paper"    and computer == "rock"):
            print(f"You win this round!")
            player_score += 1
        elif (player == "scissors" and computer == "paper"):
            print(f"You win this round!")
            player_score += 1
        else:
            computer_score += 1
            print(f"Computer wins this round!")

    print(f"\nFinal Score  -  You: {player_score}  |  Computer: {computer_score}")
    if player_score == 3:
        print("Congratulations! You won the game!")
    else:
        print("Computer wins the game! Better luck next time.")

    again = input("\nPlay again? (yes / no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break