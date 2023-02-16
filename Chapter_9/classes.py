# Exercises 9-1 .. 9-3

# Exercises 9-1 and 9-2
print('Exercises 9-1 and 9-2')

class Restaurant:
    """TBD"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize instance of class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name} is now open!")


restaurant = Restaurant('Biagio', 'Italian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('\n')

# Make three new instances of the class
restaurant_2 = Restaurant('McDonalds', 'American')
restaurant_3 = Restaurant('Mios','Greek')
restaurant_4 = Restaurant('Jakes', 'Canadian')

# Run describe_restaurant() for each instance
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_4.describe_restaurant()
print('\n')


# Exercise 9-3: Users
print('Exercise 9-3')

class User:
    """TBD"""

    def __init__(self, first_name, last_name, age, password, mother_maiden_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.mother_maiden_name = mother_maiden_name

    def describe_user(self):
        """Prints a summary of the user's information"""
        full_name = f'{self.first_name.title()} {self.last_name.title()}'

        print(f'Info on user: {full_name}')
        print(f'    First name: {self.first_name.title()}')
        print(f'    Last name: {self.last_name.title()}')
        print(f'    Age: {self.age}')
        print(f'    Password: {self.password}')
        print(f"    Mother's maiden name: {self.mother_maiden_name}")
        print('\n')
        

    def greet_user(self):
        print(f'Well, hello there, {self.first_name.title()}!')
        print('\n')

# Create instances of several different users, and call both methods for each user
person_1 = User( 'Jeff', 'salamander', 25, '1234', 'Smits')
person_1.describe_user()
person_1.greet_user()

person_2 = User( 'Jorff', 'stamander', 2, '12345', 'Smiths')
person_2.describe_user()
person_2.greet_user()

person_3 = User( 'Jeorg', 'ster', 55, '441234', 'Smiz')
person_3.describe_user()
person_3.greet_user()
