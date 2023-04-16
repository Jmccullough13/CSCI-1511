#User login
#Jeffrey McCullough
#This program asks for a username and its associated password. If either is not in the dictoinary, the program ends. If both are correct, the user is assigned a security level, with 10 being the lowest.
#February 14, 2023

import random
user_info = {
    'ayankovic': 'AccordiansRule',
    'mjackson': 'BeatItBad',
    'dlroth': 'JmpngWthThDdvl!',
    'pbenetar': 'ShadowsBreaker',
    'kbush': 'BaWutheringHills',
}

user = input("Enter your user name: ")
if user in user_info:
    user_pw = user_info[user]
    password = input("Enter your password: ") 
    if password == user_pw:
        security = random.randint(1, 10)
        print(f"Welcome {user}! Your security level is {security}.")
    else:
        print("That password is incorrect.")
elif user == "guest":
    password = input("Enter your password: ")
    if password == "guest":
        print(f"Welcome guest! Your security level is 10, the lowest level of security.")
    else:
        print("That is the wrong password.")
else:
    print("The user does not exist")