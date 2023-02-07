#Car Sale Calculator
#Jeffrey McCullough
#January 16, 2023

cost = input("Cost of car: ")
tax = int(float(cost) * .065)
destination = 1000
title = 15
licensing = int(float(cost) * .03)
prep = 250
total = int(cost) + destination + title + licensing + prep

print(f"Car price: ${cost}\nTax: ${tax}\nTitle Fee: ${title}\nLicense Fee: ${licensing}\nDealer Documentation Preperation Fee: ${prep}\nDestination Fee: ${destination}\nTotal Costs: ${total}")
