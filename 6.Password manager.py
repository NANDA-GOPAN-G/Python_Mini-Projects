'''The following code is just beginner level password manager which will be upgraded to an advanced level one in time.''' 

from cryptography.fernet import Fernet
'''
key + password + text to encrypt = encrypted text
random text + key + password = text to encrypt
'''

"""
# used to create the key file.
def write_key():
    key  =  Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()
"""

def load_key():
    file =  open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def add():
    name = input("Account name:- ")
    pwd = input("Password:- ")

    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("USERNAME:",user,"\nPASSWORD:",
                fer.decrypt(passw.encode()).decode())

while True:
    mode = input("Would you like to add a new password or view existing ones or quit(view/add/quit)?: ").lower()
    if mode == "quit":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("INVALID MODE...")
        continue

