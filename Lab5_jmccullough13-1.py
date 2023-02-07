#Dice Roll
#Jeffrey McCullough
#This program will simulate two dice rolling, show the dice roll and the total, and print a term based on the roll results. When finished, the user is prompted to roll again or quit.
#January 30, 2023

import random
again = True
while again:
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    print(f"You rolled {roll_1} and {roll_2}")
    if roll_1 + roll_2 == 2:
        print(roll_1 + roll_2)
        print("Snake Eyes")
    elif roll_1 + roll_2 == 3:
        print(roll_1 + roll_2)
        print("Ace Caught a Deuce")
    elif roll_1 == 2 and roll_2 == 2:
        print(roll_1 + roll_2)
        print("Little Joe from Kokomo")
    elif roll_1 + roll_2 == 5:
        print(roll_1 + roll_2)
        print("Little Phoebe")
    elif roll_1 == 3 and roll_2 == 3:
        print(roll_1 + roll_2)
        print("Jimmy Hicks from the Sticks")
    elif roll_1 == 6 and roll_2 == 1:
        print(roll_1 + roll_2)
        print("Six Ace")
    elif roll_1 == 1 and roll_2 == 6:
        print(roll_1 + roll_2)
        print("Six Ace")
    elif roll_1 == 4 and roll_2 == 4:
        print(roll_1 + roll_2)
        print("Eighter from Decatur")
    elif roll_1 + roll_2 == 9:
        print(roll_1 + roll_2)
        print("Nina from Pasadena")
    elif roll_1 == 5 and roll_2 == 5:
        print(roll_1 + roll_2)
        print("Puppy Paws")
    elif roll_1 + roll_2 == 11:
        print(roll_1 + roll_2)
        print("Six Five no Jive")
    elif roll_1 + roll_2 == 12:
        print(roll_1 + roll_2)
        print("Boxcars")
    else:
        print(roll_1 + roll_2)
    
    go_again = input("Do you want to roll again? Type anything to roll again or quit to exit: ")
    if str(go_again.lower()) == "quit":
        again = False
        print("Thanks for playing!")
    else:
        again = True