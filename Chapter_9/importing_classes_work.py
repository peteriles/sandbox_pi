"""Importing class work. Exercises 9-10 through 9-12"""


# Exercise 9-10
print('Exercise 9-10')

import restaurant

my_restaurant = restaurant.Restaurant('Biagio', 'Italian')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print('\n')

# Exercise 9-11 (and now updated to support Excercise 9-12)
print('Exercise 9-11 and 9-12')

import detailed_users

# Create an admin
my_admin = detailed_users.Admin(
    'pedro', 'eels', 20, 'gorby1234', 'hannah', 
    ['can ban user', 'can delete post', 'can delete database'])
my_admin.describe_user()
my_admin.increment_login_attempts()
print(f'Login attempts: {my_admin.login_attempts}')
my_admin.privileges.show_privileges()

