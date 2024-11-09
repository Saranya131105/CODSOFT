import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
print("Welcome to Rock-Paper-Scissors!")
print("Instructions: Enter 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' to stop playing.\n")
while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice == "exit":
        print("Thank you for playing!")
        break
    elif user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    print(result)
    print(f"Score: You {user_score} - Computer {computer_score}\n")
print("\nFinal Score:")
print(f"You: {user_score} | Computer: {computer_score}")
print("Goodbye!")