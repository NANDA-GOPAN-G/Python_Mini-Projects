import random

print("_______________WELCOME TO ROCK-PAPER-SCISSORS_______________")
print(".\n.\n.")
print("______________________STARTING THE GAME_____________________")
print(".\n.\n.")
user_score = 0
computer_score = 0
options = ["ROCK", "PAPER", "SCISSORS"]
username = input("ENTER THE PLAYER NAME:-  ")

while True:
    user_input = input("\nType ROCK / PAPER / SCISSORS or Q to stop the game:-  ").upper()

    if user_input == "Q":
        break

    if user_input not in options:
        print("\nERROR..PLEASE ENTER ROCK / PAPER / SCISSORS / Q..")
        continue

    random_num = random.randint(0, 2)
    """
    ROCK : 0
    PAPER : 1
    SCISSORS : 2
    """
    computer_input = options[random_num]
    print("\nCOMPUTER PICKED",computer_input,".")

    if user_input == "ROCK" and computer_input == "SCISSORS":
        print("\nYou Won!")
        user_score += 1
    elif user_input == "PAPER" and computer_input == "ROCK":
        print("\nYou Won!")
        user_score += 1
    elif user_input == "SCISSORS" and computer_input == "PAPER":
        print("\nYou Won!")
        user_score += 1
    elif user_input == computer_input:
        continue
    else:
        print("\nComputer Wins!")
        computer_score += 1

print("\nYOU WON", user_score, "TIMES")
print("COMPUTER WON", computer_score, "TIMES")

if user_score > computer_score:
    print("\nCONGRATULATIONS,", username, ",YOU ARE THE WINNER...")
elif  user_score < computer_score:
    print("\nSORRY", username, ",YOU LOST THE GAME...")
else:
    print("\nOOPS... ITS A DRAW")
print("\n\n....................EXITING GAME....................")







