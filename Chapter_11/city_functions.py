# Exercises 11-1 and 11-2

def city_info(city, country, population=''):
    """Return a neatly-formatted string"""
    if population:
        neat_string = f'{city.title()}, {country.title()} - population {population}'
    else:
        neat_string = f'{city.title()}, {country.title()}'
        
    return neat_string