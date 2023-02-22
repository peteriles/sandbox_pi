# Exercises 8-12 .. 8-14

# Exercise 8-12: Sandwiches
print('Exercise 8-12')

def print_sandwich_items(*items):
    """Print arbitrary number of items on a sandwich"""
    print(f'Tuple of items is: {items}')
    
    print('Individual items are:')
    for item in items:
        print(f'    {item}')


# Call function three times
print_sandwich_items('tomato')
print_sandwich_items('lettuce','peppers','cheese')
print_sandwich_items('PB','jam','onions','cheese')

print('\n')


# Excercise 8-13: User profile
print('Exercise 8-13')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    
    print(f'Dictionary that was passed into the function: {user_info}')
    
    # Add new items to the dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last

    print(f'Modified dictionary: {user_info}')

    return user_info

profile = build_profile('pete', 'jones', height="tall", shoes="big", hair=5)

print(f'Profile is: {profile}')


# Exercise 8-14: Cars
print('Exercise 8-14')

def store_car_info(manufacturer, model_name, **kwargs):
    """Build dictionary of car info and print it"""
    print(f'Arbitrary keyword dictionary is: {kwargs} ')

    # Add to the arbitrary-keyword dictionary
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name

    print(f'Updated dictionary is {kwargs}')

    return kwargs

car = store_car_info('subaru', 'outback', color='blue', tow_package=True)
print(f'Returned dictionary is: {car}')