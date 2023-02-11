# Exercises 5-3 .. 5-7

# 5-3
print("Exercise 5-3")
#alien_colour = 'green'
alien_colour = 'yellow'

if alien_colour == 'green':
    print("You just earned 5 points!")

# 5-4
print("Exercise 5-4")
alien_colour = 'yellow'

if alien_colour == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# 5-5
print("Exercise 5-5")
#alien_colour = 'yellow'
alien_colour = 'red'

if alien_colour == 'green':
    print('You got 5 points!')
elif alien_colour == 'yellow':
    print("You just got 10 points!")
elif alien_colour == 'red':
    print("You just got 15 points!")
else:
    print("You got 0 points.")

# 5-6
print("Exercise 5-6: Stages of life.")
age = 15
assert(type(age)==int)

if age < 2:
    category = "a baby"
elif age < 4:
    category = "a toddler"
elif age < 13:
    category = "a kid"
elif age < 20:
    category = "a teenager"
elif age < 65:
    category = "an adult"
elif age >= 65:
    category = "an elder"
else:
    category = "UNKNOWN"

print(f"The person is {category}.")

# 5-7: Favourite fruit
fave_fruits = ['grapefruit','orange','pomegranate','grape','raspberry']
#fruit = 'grapefruit'
#if fruit in fave_fruits:
#    print(f"{fruit.title()} is in the list!")

if 'grapefruit' in fave_fruits:
    print('Grapefruit is in the list!')
else:
    print('Grapefruit is not in the list.')
    
if 'melon' in fave_fruits:
    print('Melon is in the list!')
else:
    print('Melon is not in the list.')

if 'raspberry' in fave_fruits:
    print('Raspberry is in the list!')
else:
    print('Raspberry is not in the list.')

if 'strawberry' in fave_fruits:
    print('Noice! You love strawberryies.')
else:
    print('You are not a fan of strawberries.')

if 'orange' in fave_fruits:
    print("Yes! You love oranges!")
else:
    print("Oranges ain't your thing.")





