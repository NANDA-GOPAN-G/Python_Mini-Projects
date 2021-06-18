import random

while True:
    roll = input("\nDO YOU WISH TO ROLL THE DICES(Yes/No)?\n").lower()

    if roll == "yes":
        print("\nROLLING THE DICES...")
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print("\nTHE VALUES ARE......",d1,"and",d2)
        continue

    elif roll == "no":
        print("EXITING...")
        quit()

    else:
        print("INVALID CHOICE...")
        print("PLEASE ENTER A VALID CHOICE")
        
