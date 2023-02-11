# Exercises 5-8..5-10

# Exercise 5-8, 5-9: Hello Admin
usernames = ['piles','Jsmith','harevco','fsalus','dpigeon','ggorovov','admin']
#usernames = []

if usernames:
    for user in usernames:
        print(f"Hello {user}, ")
        if user == 'admin':
            print('would you like to see a status report?')
        else:
            print('thanks for logging in again.')
else:
    print('No usernames in list.')

# Exercise 5-10
current_users = usernames[:]
current_users.append('rsampson')

print(f"Current users: {current_users}")

# Make lower-case version of current_users
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

print(f"Current users (lowercase): {current_users_lower}")
#print(usernames)

new_users = ['ttrayvon','glo','dpigeon','fsalus2','rsampson','JSMITH']

for new_user in new_users:
    # Check lower-case version of names in both current and new user lists
    if new_user.lower() in current_users_lower:
        print(f'This username, {new_user}, has already been used. You need to enter a new username.')
    else:
        print(f'This username, {new_user}, is available!')