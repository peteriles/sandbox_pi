# Exercises 7-8 .. 7-10

# Exercise 7-8
print('Exercise 7-8')

sandwich_orders = ['ham', 'club', 'PB&J', 'roast beef', 'cheese']
finished_sandwiches = []

# Loop over all orders until list is empty
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'I have made your {order} sandwich!')

    finished_sandwiches.append(order)

print(f"Here are all the sandwiches that have been made: {finished_sandwiches}")
print(f"Here are all the sandwiches still to make: {sandwich_orders}")
print('\n')

# Exercise 7-9
sandwich_orders = ['pastrami', 'ham', 'pastrami', 'club', 'PB&J', 'pastrami']
finished_sandwiches = []

print('The deli has run out of pastrami!!')

# Loop over all orders
while sandwich_orders:
    
    order = sandwich_orders.pop()

    if order == 'pastrami':
        print("No!! We can't make a pastrami sandwich.")
    else:
        finished_sandwiches.append(order)
        print(f"I have made your {order} sandwich!")

print(f"Here are all the sandwiches that have been made: {finished_sandwiches}")
print(f"Here are all the sandwiches still to make: {sandwich_orders}")
print('\n')

# Exercise 7-10: Dream vacation
print("Exercise 7-10")
print("Welcome to our poll!")
poll = {}
poll_flag = True

while poll_flag == True:
    name = input('Enter your name: ')
    location = input('Where would you like to go? ')

    # Add result to the dictionary
    poll[name] = location

    response = input('Would you like to let someone else answer (yes/no)? ')

    if response == 'no':
        poll_flag = False

for person, location in poll.items():
    print(f'Person: {person}; Location: {location}')