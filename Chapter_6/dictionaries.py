# Exercises 6-1 .. 6-12

# 6-1: Person
print('Exercise 6-1')
person = { 
    'first_name':'scootie', 
    'last_name':'graffics', 
    'age':'30', 
    'city':'singapoon',
    }

# Print each key-value pair
for key in person:
    print(f'Key is: {key}; value is: {person[key]}')

print('\n')


# 6-2: Favourite numbers
print('Exercise 6-2')
fave_nums = {} # Create an empty dictionary to start with
fave_nums['pete'] = 139
fave_nums['ted'] = 7
fave_nums['inigo'] = 6
fave_nums['frodo'] = 1
fave_nums['voldemort'] = 6

# Print names and fave nums
for key in fave_nums:
    print(f"{key.title()}'s favourite number is {fave_nums[key]}")

# Test removing a key-value pair
print(fave_nums['voldemort'])
del fave_nums['voldemort']
# print(fave_nums['voldemort']) # This will generate a KeyError
print(fave_nums.get('voldemort','Sorry, this key does not exist'))
print('\n')


# 6-3, 6-4: Glossary
print('Exercises 6-3 and 6-4')
glossary = {
    'language':'python',
    'tuple':'cannot be changed',
    'list':'can be changed',
    'dictionary':'filled with key-value pairs',
    'condition':'true or false'
}

# Add some terms
glossary['set'] = 'unique items only'
glossary['hamburger'] = 'tasty'
glossary['default'] = 'what happens with no input'

#for key in glossary:  # This is fine
for word in glossary.keys():
    print(f'The definition of {word} is {glossary[word]}\n')

    if word == 'list':
        glossary['list'] = 'see, it just changed!'
        print(f'The definition of {word} is {glossary[word]}\n')

print('\n')


# Exercise 6-5: Rivers
print('Exercise 6-5')
rivers = { 'nile': 'egypt', 'amazon': 'brazil', 'yukon': 'canada'}

for river in rivers.keys():
    print(f'The {river.title()} runs through {rivers[river].title()}')

print('The names of all rivers in the dictionary are:')
for river in rivers.keys():
    print(river)

print('The names of all countries in the dictionary are:')
for country in rivers.values():
    print(country)

print('The names of rivers and their associated countries are:')
for river, country in rivers.items():
    print(river)
    print(country)

print('\n')


# Exercise 6-6: Polling
print('Exercise 6-6')
fave_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
print(f'People who have taken the poll: {list(fave_languages.keys())}')

polling_list = [ 'jen', 'peter', 'phil', 'raj', 'stuart']
print(f'People to check if they have taken the poll: {polling_list}')

for name in polling_list:
    if name in fave_languages:
        print(f'Thanks, {name.title()}, for taking the poll!')
    else:
        print(f'{name.title()}, please take this poll!!')

print('\n')

# Exercise 6-7
print('Exercise 6-7')

# Make three separate dictionaries, one per person
person_1 = { 
    'first_name': 'scootie', 
    'last_name': 'graffics', 
    'age': '30', 
    'city': 'singapoon',
    }

person_2 = {
    'first_name': 'raymo',
    'last_name': 'cadena',
    'age': 20,
    'city': 'madrid',
    }

person_3 = {
    'first_name': 'dev',
    'last_name': 'patil',
    'age': 42,
    'city': 'toronto',
    }

# Put all three dictionaries in a list
people = [ person_1, person_2, person_3]

for human in people:
    full_name = f"{human['first_name'].title()} {human['last_name'].title()}"
    print(f'Full name: {full_name}')
    print(f"Age: {human['age']}")
    print(f"City: {human['city'].title()}")
    print('\n')


# Exercise 6-8
print('Exercise 6-8')

pet_1 = {
    'name': 'orion',
    'age': 18,
    'type': 'cat',
    'owner': 'dev',
    }

pet_2 = {
    'name': 'rigel',
    'age': 3,
    'type': 'dog',
    'owner': 'shira',
    }

pet_3 = {
    'name': 'deneb',
    'age': 10,
    'type': 'rat',
    'owner': 'gus'
    }

# List of dictionaries
pets = [ pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"Age: {pet['age']}")
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print('\n')


# Exercise 6-9
print('Exercise 6-9')

# Make a dictionary of lists
fave_places = { 
    'trace': [ 'korea', 'rockies'], 
    'rusty': [ 'yukon', 'india', 'alaska'], 
    'hells': ['yukon'], 
    'ritts': ['mom and dad bed'],
    'petra': ['sault ste. marie','ottawa'],
    }

# Loop through keys in the dictionary
for name in fave_places.keys():
    print(f'Name: {name}')

    # Extract list at the current key
    places = fave_places[name]

    # Loop through items in the list
    for place in places:
        print(f'    Fave place: {place}')


# Exercise 6-10
print('Exercise 6-10')

# Create a dictionary of lists
fave_nums2 = {}
fave_nums2['pete'] = [4, 3, 1]
fave_nums2['grant'] = [12, 22, 120]
fave_nums2['toyo'] = [1, 0, 44, 66, 139]

# Loop over all keys (people)
for person in fave_nums2.keys():
    print(f'Person is: {person}')
    
    # Extract the list of the fave nums for the current person
    individual_fave_nums = fave_nums2[person]

    if person == 'toyo':
        print(f"    Adding an extra fave num for {person}")
        individual_fave_nums.append(55)

    # Loop over all the fave nums
    for num in individual_fave_nums:
        print(f'    Fave num: {num}')


# Exercise 6-11: Cities
print('Exercise 6-11')

cities = {
    'ottawa': {
        'population': 1_000_000,
        'fact': 'has a long skating rink',
        'country': 'canada',
        },
    'miami': {
        'population': 2_000_000,
        'fact': 'by the ocean',
        'country': 'usa',
        },
    'tokyo': {
        'population': 10_000_000,
        'fact': 'fast trains',
        'country': 'japan',
        },
    }

# Loop over all keys (cities) in main dictionary
for city in cities.keys():
    print(f'City is: {city}')

    # Extract the dictionary for the current city
    curr_city = cities[city]

    # Loop over all keys (categories) in each city's dictionary
    for category,value in curr_city.items():
        print(f'    {category} is {value}')
