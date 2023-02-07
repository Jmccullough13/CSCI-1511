#Rivers Dictionary
#Jeffrey McCullough
#This program creates a dictionary of rivers and the countries they're in, prints the names of rivers and countries, and a sentence about the river and the country togather.
#February 6, 2023

rivers = {'nile': 'egypt', 'rhine': 'france', 'severn': 'england', 'missouri': 'the united states of america'}
for river in rivers.keys():
    print(f"the {river.title()} River")
for country in rivers.values():
    print(country.title())
for river, country in rivers.items():
    print(f"The {river.title()} River is the longest river in {country.title()}")