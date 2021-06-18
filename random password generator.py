"""This code is to generate a password using random letters/numbers/symbols in the variable 'S' """

import random

print("_______________BASIC PASSWORD GENERATOR_______________")
print(".\n.\n.")

pwd_length = int(input("ENTER THE LENGTH OF THE PASSWORD: "))
S = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(S,pwd_length))
print("\nPASSWORD GENERATED:-\n" + password)
print(".\n.\n.")
print("EXITING PASSWORD GENERATOR....")
