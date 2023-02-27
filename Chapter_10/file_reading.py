# Exercises 10-1 through 10-3
from pathlib import Path

# Exercise 10-1
print('Exercise 10-1')

file_path = Path('Chapter_10/learning_python.txt') # This file is in the current directory
file_contents = file_path.read_text()

# Print entire contents of file
print(file_contents)

# Print each line individually
for line in file_contents.splitlines():
    print('Current line is: ', line)

print('\n')

# Exercise 10-2
print('Exercise 10-2')

# Print each line individually, but swap out some text
for line in file_contents.splitlines():
    mod_line = line.replace('Python', 'Ruby')
    print('Current line is: ', mod_line)

print('\n')


# Exercise 10-3
print('Exercise 10-3')

# This exercise was just to remove temp variables and loop
# directly over the returned variable from splitlines()