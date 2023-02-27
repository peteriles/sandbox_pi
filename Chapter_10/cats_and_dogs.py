# Excercises 10-8 .. 10-9
from pathlib import Path

print('Exercise 10-8 and 10-9')
cat_file_path = Path('Chapter_10/cats.txt')
dog_file_path = Path('Chapter_10/dogs.txt')


try:
    cat_text = cat_file_path.read_text()
    dog_text = dog_file_path.read_text()

except FileNotFoundError:    
    #print("Shoot, one or both of the files do not exist.")
    pass # Catch the exception silently

else:
    print('Cat text file contents: ')
    print(cat_text)
    print('\n')

    print('Dog text file contents: ')
    print(dog_text)

print('\n')
print('The program is complete')
print('\n')