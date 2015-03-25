from random import randint

def rps(choice):
    choices = { "rock": 0, "paper": 1, "scissors": 2 }
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = randint(0, 2)
    print("Computer chooses", computer_choices[computer_choice])
    result = choices[choice] - computer_choice
    if result == -2:
        result = 1
    if result == 0:
        print("Tie")
    elif result == 1:
        print("Win")
    else:
        print("Lose")

rps(input("Make your choice: "))
