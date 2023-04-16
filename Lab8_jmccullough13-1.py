#UPC Scanner
#Jeffrey McCullough
#The program takes an entered number, passes it into a function, checks to see if the length of the number is a valid UPC length, and lets the user know if it's valid or not.
#February 20, 2023

def find_upc(bar_code):
    """Check a UPC to determine it's validity."""
    if len(bar_code) == 12:
        print(f"{bar_code} is a valid UPC.")
    else:
        print(f"{bar_code} is not a valid UPC.")

while True:
    upc = input("Enter the UPC code or type 'q' to quit: ")
    if upc.upper() == "Q":
       break
    else:
        find_upc(upc)
