#Father Finder
#Jeffrey McCullough
#This program contains a dictionary of names of people and their fathers. Users will choose and option and enter a name and the program will return the name of the 
#person's father or grandfather, if in the dictionary, a list of all of the sons in the dictionary, or quit. If an invlalid choice is entered, they will be prompted for a new choice.
#February 6, 2023

sons_and_fathers = {
    'John Quincy Adams': 'John Adams', 
    'Bart Simpson': 'Homer Simpson', 
    'Homer Simpson': 'Abe Simpson', 
    'John Adams': 'John Adams Sr.',
    'Harry Potter': 'James Potter',
    'Albus Potter': 'Harry Potter',
    'Atreus': 'Kratos',
    'Kratos': 'Zeus',
    'Gohan': 'Goku',
    'Goku': 'Bardock',
    'Trunks': 'Vegeta',
    'Vegeta': 'King Vegeta'
}
print("\tFather Finder\n")
while True:
    choice = input("\tChoose an option\n\t0 - Quit\n\t1 - Find a Father\n\t2 - Find a Grandfather\n\t3 - List all of the sons/keys\n\nChoice: ")
    if choice == "1":
        son = input("Enter the son's name: ")
        if son in sons_and_fathers:
            father = sons_and_fathers[son]
            print(f"His father is {father.title()}\n")
            continue
        else:
            print("Don't know who their father is. Try again.\n")
    elif choice == "2":
        grandson = input("Enter the grandson's name: ")
        if grandson in sons_and_fathers:
            father = sons_and_fathers[grandson]
            if father in sons_and_fathers:
                grandfather = sons_and_fathers[father]
                print(f"His grandfather is {grandfather.title()}\n")
                continue
            else:
                print("Don't know who their grandfather is. Try again.\n")
        else:
            print("Don't know who their grandfather is. Try again.\n")
    elif choice == "3":
        for son, father in sons_and_fathers.items():
            print(son.title())
            continue
    elif choice == "0":
        print("Thank you, good bye.")
        break
    else:
        print("Invalid choice")
