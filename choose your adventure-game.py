def bear_room():
    print("You reached another room. And here in this room there is a Bear.")
    print("Behind the bear there is another door.")
    print("The bear is eating honey happily which seems very tasty..")
    print("What would you do?(choose 1 or 2)")
    print("1. Take the honey")
    print("2. Taunt the bear")

    bear = int(input(">"))

    if bear == 1:
        gameover("\nThe bear killed you for taking its honey.\n...You died...")
    elif bear == 2:
        print("\nYour Good Time,the bear moved from the door. You can go through it now!")
        diamond_room()
    else:
        gameover("You wasted your time thinking the impossible and the bear killed you after finishing its honey.\nChoose whats possible in your next life")

def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")

    answer = input(">")

    if answer == "1":
        diamond_room()
    elif answer == "2":
        gameover("The monster was hungry, he/it ate you.")
    else:
        gameover("You wasted your time thinking the impossible and the monster wake up from ist sleep after some time.\nThen it ate you.")

def diamond_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")

    answer = input(">")

    if answer == "1":
        gameover("They were cursed diamonds!\nThe moment you touched it, the disintegrated..., and you died!")
    elif answer == "2":
        print("\nNice, you're are an honest man!\nYou win the game!")
        print("----------YOU WON----------")
        print("------CONGRATULATIONS------")
        play_again()
    else:
        gameover("Still wasting your time thinking the impossible. You lose...")

def gameover(reason):
    print("\n",reason)
    print("\n----------GAME OVER----------")
    play_again()

def play_again():
    print("\nDo you want to play again? (yes or no)")

    answer = input(">").lower()

    if "yes" in answer:
        start()
    else:
        quit()

def start():
    print("\nYou are standing alone in a small very spooky room...")
    print("There is a door to your left and to your right. Which door would you choose?(choose 1 or 2)")
    print("1. Left door\n2. Right door")
    door = int(input(">"))
    if door == 1:
        bear_room()
    elif door == 2:
        monster_room()
    else:
        gameover("No door exists in that direction.\nYou died of heart attack by getting scared...\nTry again in next life")


print("_______________ADVENTURE TIME_______________")
print(".\n.\n.\n.\n.")
player = input("Enter the Player's name:  ")
print(".\n.\n.")
print("WELCOME",player.upper())
print("...TYPE 'YES' TO PLAY THE GAME...")
ready = input().lower().strip()
if ready != "yes":
    print("_________________EXITING GAME________________")
    quit()
start()




