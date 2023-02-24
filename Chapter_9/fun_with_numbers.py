"""Exercises 9-13 through 9-16"""
from random import randint # Exercise 9-13
from random import choice # Exercise 9-14

# Exercise 9-13
print('Exercise 9-13')

class Die:
    """A simple model of a Die"""

    def __init__(self, sides=6):
        """Initialize attributes"""
        self.sides = sides

    def roll_die(self):
        roll_value = randint(1, self.sides)
        print(f'The value rolled is {roll_value}')


#my_standard_die = Die()
#my_standard_die = Die(10)
my_standard_die = Die(20)

# Roll the die 10 times
for i in range(10):
    print(f"Roll number {i+1}: ")
    my_standard_die.roll_die()

print('\n')


# Exercise 9-14, and updated for Exercise 9-15
print('Exercises 9-14 and 9-15')

def generate_winning_sequence():
    """Function to generate a winning lottery sequence"""
    
    # Hard-code the available numbers and letter from which to draw from
    list_of_stuff = [ 
        'a', 'c', 'b', 'r', 'y', '3', '5', '8', '1', '23', 
        '676', '77', '123', '543', '138'
        ]

    winning_sequence = []
    done = False
    counter = 0

    while done == False:
        counter += 1
        #print(f'Iteration number {counter}')
        selected_item = choice(list_of_stuff)

        if selected_item in winning_sequence:
            #print('Note: Duplicate item; choosing another one.')
            pass
        else:
            # Add selected value to the winning list
            winning_sequence.append(selected_item)

        if len(winning_sequence) == 4:
            # We have enough items in the winning list; so we're done
            done = True

    print(f'The winning sequence is: {winning_sequence}')
    
    return winning_sequence

# See how many lottery iterations we need to have my ticket win
max_num_iterations = 10000 # Note, in one test, I got the winning combo in iteration 3057 :)

my_ticket = ['a', 'c', 'b', 'r']

# Iterate over randomly-generated winning tickets
for iteration in range(max_num_iterations):
    print(f'Iteration number {iteration+1}')

    winning_ticket = generate_winning_sequence()

    # Check to see if all my individual numbers/letters are in the winning ticket
    matched_value_count = 0

    # Count number of matching values
    for my_number_or_letter in my_ticket:
        if my_number_or_letter in winning_ticket:
            matched_value_count += 1

    if matched_value_count == 4:
        print('All 4 values match: I won!')
        break;
    else:
        print(f'Darn, only {matched_value_count} value(s) match(es).')
