#Guess My Number
#Jeffrey McCullough
#This program generates a random number and asks the user to guess it. If too high or low, the program tells the user and prompts another response. If correct, the program prints the number of guesses and ends the program.
#February 14, 2023

import random
comp_num = random.randint(1, 100)
user_num = int(input("Guess a number between 1 and 100: "))
guesses = 1
while True:
    if user_num > 100 or user_num < 1:
        user_num = int(input("Please enter a number between 1 and 100: "))
    elif user_num != comp_num and user_num < comp_num:
        guesses += 1
        user_num = int(input("Too low. Guess again: "))
    elif user_num != comp_num and user_num > comp_num:
        guesses += 1
        user_num = int(input("Too high. Guess again: "))
    else:
        print(f"Congratulations, the number was {comp_num}.\nNumber of guesses: {guesses}.")
        break