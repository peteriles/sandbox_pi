# Exercises 10-4 and 10-5
from pathlib import Path

# Exercise 10-4
print('Exercise 10-4')

name = input("Hello there. Please enter your name: ")

file_path = Path("guest.txt") # Create Path object

file_path.write_text(name)

print('\n')


# Exercise 10-5
print ('Exercise 10-5')
prompt_active = True
file_path_2 = Path("guest_book.txt")
text_to_write = ''

while prompt_active == True:
    name = input("Hi again. Please enter your name ('q' to quit): ")

    if name == "q":
        break

    text_to_write += (name + '\n')

file_path_2.write_text(text_to_write)

print('\n')

