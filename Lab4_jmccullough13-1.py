#Deal Cards
#Jeffrey McCullough
#This is a program that will ask a user for the size of a hand of cards and print a list of cards in the hand
#January 23, 2023

import random
card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_suit = ["c", "h", "s", "d"]
x = input("Enter the number of cards in your hand: ")
for card in range (0, int(x)):
    print(f"{random.choice(card_value)}{random.choice(card_suit)}")