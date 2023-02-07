#Tip Calculator
#Jeffrey McCullough
#January 17, 2023

total = input("Amount of bill: ")
tip_15 = (round(float(total) * .15, 2))
tip_20 = (round(float(total) * .2, 2))
total_15 = (round(float(total) + tip_15, 2))
total_20 = (round(float(total) + tip_20, 2))

print(f"Your total for the meal is ${total}. \nSuggested tips: \n15%: ${tip_15}\n\tTotal with this tip ${total_15}\n20%: ${tip_20}\n\tTotal with this tip ${total_20}\nThank you and have a nice day!")