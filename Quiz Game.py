print("------------------------WELCOME TO MY COMPUTER QUIZ GAME------------------------")
print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.")

play = input("Are you ready to play?(Yes/No)  ").lower()
if play != "yes":
  print("..................................EXITING GAME..................................")
  exit()

score = 0
name = input("\nEnter Player Name:  ")


answer = input("\nWHO IS KNOWN AS 'THE FATHER OF COMPUTER'? ").lower()
if answer == "charles babbage":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")
  
answer = input("\nWHAT DOES CPU STAND FOR? ").lower()
if answer == "central processing unit":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

answer = input("\nWHAT DOES GPU STAND FOR? ").lower()
if answer == "graphics processing unit":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")
    
answer = input("\nWHAT DOES RAM STAND FOR? ").lower()
if answer == "random access memory":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

answer = input("\nWHAT DOES ROM STAND FOR? ").lower()
if answer == "read only memory":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

if score == 5:
    print(f"\nWELL PLAYED UNTIL NOW {name}.. \n LETS CONTINUE.")


print("\nIMPORTANT: For the next set of questions, please answer by entering the answer and not by entering option number.")

print("\nWHICH ONE IS THE FIRST SEARCH ENGINE IN INTERNET?")
print("(a) Google \n(b) Archie \n(c) Altavista \n(d) WAIS")
answer = input().lower()
if answer == "archie":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

print("\nTHE FIRST MECHANICAL COMPUTER DESIGNED BY CHARLES BABBAGE WAS CALLED?")
print("(a) Abacus \n(b) Analytical Engine \n(c) Calculator \n(d) Processor")
answer = input().lower()
if answer == "analytical engine":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

print("\nWHICH OF THE FOLLOWING IS AN EXAMPLE OF NON-VOLATILE MEMORY?")
print("(a) VLSI \n(b) LSI \n(c) ROM \n(d) RAM")
answer = input().lower()
if answer == "rom":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

print("\nFPI STANDS FOR?")
print("(a) Frames per inch \n(b) Faults per inch \n(c) Figure per inch \n(d) Film per inch")
answer = input().lower()
if answer == "frames per inch":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")

print("\nTHE FIRST MOVIE RELESED IN 1982 WITH TERRIFIC COMPUTER ANIMATION AND GRAPHICS WAS?")
print("(a) Star Wars \n(b) Tron \n(c) Forbidden Planet \n(d) Dark Star")
answer = input().lower()
if answer == "star wars":
    print("CORRECT ANSWER")
    score += 1
else:
    print("INCORRECT ANSWER")


print(f"\nCONGRATUALTIONS {name}.... {score}/10 QUESTIONS ARE CORRECT")
if score == 10:
    print("\nEXCELLENT GAME.... YOU ARE A GENIUS")
elif score >= 7:
    print("\nGOOD GAME.. \nWELL DONE.")
elif score >= 5:
    print("\nNICE GAME.. \nBETTER LUCK NEXT TIME")
else:
    print("\nBETTER LUCK NEXT TIME")
print("\n..................................EXITING GAME..................................")

