#Cities Dictionary
#Jeffrey McCullough
#This program contains a dictionary of cities with information about each city and prints the information for each city.
#February 6, 2023

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '37,468,000',
        'fact': 'Tokyo was a small fishing village called Edo long ago.'
    },
    'delhi': {
        'country': 'india',
        'population': '28,514,000',
        'fact': 'Delhi has the largest spice market in Asia'
    },
    'shanghai': {
        'country': 'china',
        'population': '25,582,000',
        'fact': 'Shanghai is known as the "Magic City".'
    },
    'sao paolo': {
        'country': 'brazil',
        'population': '21,650,000',
        'fact': 'Sao Paolo is the industrial center of Brazil.'
    },
    'new york': {
        'country': 'the united states of america',
        'population': '18,819,000',
        'fact': 'New York is not in the top ten most populated cities in the world.'
    }
}
for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"{city.title()} is in {country.title()} with a population of {population}.\n{fact}")