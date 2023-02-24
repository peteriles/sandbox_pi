# Exercises 9-1 .. 9-8

# Exercises 9-1, 9-2, and 9-4
print('Exercises 9-1, 9-2, and 9-4')

class Restaurant:
    """TBD"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize instance of class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Set the value of attribute number_served"""
        self.number_served = number_served

    def increment_number_served(self, num_served_increment):
        """Increment the number of people served"""
        self.number_served += num_served_increment


restaurant = Restaurant('Biagio', 'Italian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f'This restaurant has served {restaurant.number_served} people!')
restaurant.number_served = 10
print(f'This restaurant has now served {restaurant.number_served} people!')
restaurant.set_number_served(20)
print(f"This restaurant has now served {restaurant.number_served} people! It's crazy!")
restaurant.increment_number_served(5)
print(f"This restaurant has now served {restaurant.number_served} people! I'm losing my mind!")

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


# Exercises 9-3 and 9-5: Users
print('Exercises 9-3 and 9-5')

class User:
    """TBD"""

    def __init__(self, first_name, last_name, age, password, mother_maiden_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.mother_maiden_name = mother_maiden_name
        self.login_attempts = 0

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
        """Print a message greeting the user"""
        print(f'Well, hello there, {self.first_name.title()}!')
        print('\n')

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0

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
person_3.increment_login_attempts()
person_3.increment_login_attempts()
person_3.increment_login_attempts()
print(f'The current number of login attempts is: {person_3.login_attempts}')
person_3.reset_login_attempts()
print(f'The current number of login attempts is: {person_3.login_attempts}')
print('\n')

# Exercise 9-6: Ice cream stand
print('Exercise 9-6')

class IceCreamStand(Restaurant):
    """Ice cream stand class, which is a child of the Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type, flavours):
        """
        Initialize attribute of the parent class.
        Then initialize new attributes.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def display_flavours(self):
        """Print list of flavours"""
        print(f"The available flavours are: {self.flavours}")

# Create an instance of IceCreamStand
my_stand = IceCreamStand('Creamos', 'Ice cream parlour', ['chocolate', 'vanilla', 'mint'])
my_stand.display_flavours()
print('\n')


# Exercise 9-7 and 9-8: Admin
print('Exercise 9-7 and 9-8')

class Privileges():
    """Privileges class"""

    def __init__(self, privileges):
        """Initialize attribute"""
        self.privileges = privileges

    def show_privileges(self):
        """Print the user's privileges"""

        print('The current privileges are:')
        for privilege in self.privileges:
            print(f'    Privilege: {privilege}')


class Admin(User):
    """Admin class which is a child of the User class"""

    def __init__(
            self, first_name, last_name, age, password, mother_maiden_name, 
            privileges):
        """
        Initialize attributes of the parent class.
        Then initialize attributes of the child class.
        """
        super().__init__(first_name, last_name, age, password, mother_maiden_name)

        # privileges attribute is an instance of class Privileges
        self.privileges = Privileges(privileges)
        #self.privileges = privileges

# Moved to Privileges class, below
#    def show_privileges(self):
#        """Print the user's privileges"""

#        print('The current privileges are:')
#        for privilege in self.privileges:
#            print(f'    Privilege: {privilege}')

# Create an admin
my_admin = Admin(
    'pedro', 'eels', 20, 'gorby1234', 'hannah', 
    ['can ban user', 'can delete post', 'can delete database'])
my_admin.describe_user()
my_admin.increment_login_attempts()
print(f'Login attempts: {my_admin.login_attempts}')
#my_admin.show_privileges()



my_admin_2 = Admin(
     'pedroz', 'eelsy', 25, 'gorby1444', 'gannah', 
    ['can band-aid user', 'can delete post-its', 'can make database'])
my_admin_2.privileges.show_privileges()