import random

print("__________GUESS THE NUMBER__________")
print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.")
name = input("Please, Enter your name:  ")
top_of_range = input("\nEnter the top range of the set of values:  ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("\nPLEASE ENTER A NUMBER NEXT TIME...")
    print("\nEXITING......")
    quit()

guess_count = 0
random_number = random.randint(0,top_of_range)

while True:
    user_guess = input("\nEnter your Guess:  ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\nPLEASE ENTER A NUMBER AS YOUR GUESS..")
        continue
    if random_number == user_guess:
        if guess_count == 0:
            print(f"EXCELLENT {name}.")
        print("YOUR GUESS IS CORRECT")
        break
    elif random_number < user_guess:
        print("YOU GUESSED ABOVE THE NUMBER..")
        guess_count += 1
    else:
        print("YOU GUESSED BELOW THE NUMBER..")
        guess_count += 1

print("YOU GOT IT IN",guess_count,"GUESSES")
print("\nEXITING......")
