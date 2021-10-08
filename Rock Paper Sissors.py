import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "sissors"]

while True:
    user_input = input("Type Rock/Paper/Sissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, sissors: 2
    computer_pick = options[random_number]
    print ("Computer picked ", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "sissors":
        print("You Won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        
    elif user_input == "sissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    else:
        print("You Lost!")
        computer_wins += 1

print(" ")

print("Game Summery:")

print(" ")

print("You Won", user_wins, "times.")
print("The Computer Won", computer_wins, "times.")

print(" ")

if user_wins > computer_wins:
        print("You Win!")

if computer_wins > user_wins:
        print ("You Lost!")

if user_wins == computer_wins:
        print("Tied!")

print(" ")

print("Goodbye!")
