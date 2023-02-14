# Exercises 7-4 .. 7-7

# Exercise 7-4: Pizza toppings
print('Exercise 7-4')

response = ''
while response != 'quit':
    #response = input("Please enter a topping (enter 'quit' to exit): ")
    response = 'quit' # just to move past this

    if response != 'quit':
        print(f"Adding {response} to your pizza!")
    else:
        print("Quitting.")
        

# Exercise 7-5
print('Exercise 7-5')

response = ''

while response != 'quit':
    query = "Please enter your age (enter 'quit' to quit): "
    #response = input(query)
    response = 'quit' # just to move past this
    
    # Check if they want to quit
    if response == 'quit':
        break

    # Now make sure the response is an integer
    try:
        response = int(response)
    except:
        print("Sorry, that isn't a valid number.")
        break
    
    # Check age to quote right ticket price
    cost_message = "Your ticket price is "
    if response < 3:
        cost_message += "free."
    elif response < 13:
        cost_message += "$10."
    else:
        cost_message += "$15."

    print(cost_message)


# Exercise 7-6: three exits
print("Exercise 7-6")

response = ''
num_toppings = 0

while response != 'quit':
    num_toppings += 1
    
    if num_toppings > 5:
        print("Max number of toppings reached. Exiting.")
        break

    query = "Please enter a topping (enter 'quit' to exit). "
    query += "Note: maximum 5 toppings. "
    query += "Topping: "
    response = input(query)
   
    if response == 'quit':
        print("Quitting.")
    else:
        print(f"Adding {response} to your pizza!")
    
flag = True
num_toppings = 0;

while flag == True:
    num_toppings += 1

    if num_toppings >= 5:
        flag = False

    response = input("Please enter toppings. Max 5. Topping: ")
    print(f'Adding {response} to your pizza!')


# Exercise 7-7
print("Exercise 7-7")

x = 0
# Infinite loop
while x < 2:
    print(x)

