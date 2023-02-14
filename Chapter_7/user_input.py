# Exercies 7-1 .. 7-3

# Exercise 7-1: Rental car
print('Exercise 7-1')

prompt = "What kind of rental car would you like? "

# Get response from user
#response = input(prompt)
response =  "Honda" # Just to avoid prompt

print(f"Let me see if I can get a {response} for you!")


# Excercise 7-2: Restaurant seating
print("Exercise 7-2")

prompt_2 = "How many people are in your dinner group? "

#number = input(prompt_2)
number = 4 # Just to avoid the prompt
# Make sure that "number" is actually an integer
try:
    number = int(number)
except:
    print("I'm sorry, that's not a valid number.")
    exit()

max_allowed = 8

if number > max_allowed:
    message = f"Sorry, you have more than {max_allowed} in your group. "
    message += "You'll need to wait."
    print(message)
else:
    print("Your table is ready!")


# Exercise 7-3
print("Exercise 7-3")

number_2 = input("Please enter a number: ")

try:
    number_2 = int(number_2)
except:
    print("Sorry, that isn't a valid number")
    exit()

remainder = number_2 % 10

if remainder == 0:
    print(f"Congrats, your number, {number_2}, is a multiple of 10!")
else:
    print(f"Darn; your number, {number_2}, is not a multiple of 10.")

