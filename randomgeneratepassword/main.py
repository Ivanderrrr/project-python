# ask user if they want to generate password.
# if yes, ask password length.
# generate password.
# print password.
# if no, program ended.

import string as str
import random

# method ascii_letters = concatenation of the ascii_lowercase and ascii_uppercase.
# method digits = the string "0123456789"
characters = list(str.ascii_letters + str.digits + "!@#$%^&*()" + "😁🤑🔥😎😊😂👀😒🤣😜😢😉")

# function to generate password
def generate_password():
    list_password = []
    password_length = int(input("How long do you want your password to be: "))
    
    for i in range(password_length):
        list_password.append(random.choice(characters))
    
    random.shuffle(list_password)
    new_password = "".join(list_password)

    print("\nYour password:", new_password)
    

# ask user if they want to generate password.
choices = input("Do you want to generate password (Y/N): ")

# if yes or no.
if choices.lower() == "y" or choices.lower() == "yes":
    generate_password()
elif choices.lower() == "n" or choices.lower() == "no":
    print("Program Ended, thanks....🙏")


