#Hangman
#Jeffrey McCullough
#This is a program that will simulate a game of hangman using numbers. The user will guess a number between 1 and 15 and if they are wrong, a body part will be added. Once the body is filled, the player loses.
#January 24, 2023

import random
comp_guess = random.randint(1, 15)
hangman = ["""head""", """body""", """right arm""", """left arm""", """right leg""", """left leg"""]
incorrect = 0
game_over = len(hangman)

guess = input("what is your guess? ")

while guess != None:
    if int(guess) == comp_guess:
        print("Congratulations, you win!")
        break
    else:
        print(hangman[incorrect])
        incorrect += 1
    
    if incorrect == game_over:
        print("So sorry, you lose...")
        print(f"The number was: {comp_guess}")
        break

    guess = input("what is your guess? ")
