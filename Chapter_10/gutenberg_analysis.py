# Exercise 10-10
from pathlib import Path
import os

print("Exercise 10-10")

# Load text from novels, count instances of a specific word

my_dir = 'C:\\_Personal\\Python\\other_files\\' # Need the extra "\"s since it
                                                # is an escape character
file_names_list = [ "pg145.txt", "pg70157.txt" ]

# file_1_path = Path(r'C:\_Personal\Python\other_files\pg145.txt') # This works

# Loop over all filenames in the list
for file_name in file_names_list:
    file_full_path = os.path.join(my_dir, file_name)
    
    file_path_instance = Path(file_full_path)

    try:
        file_text = file_path_instance.read_text(encoding='utf-8')
     
    except FileNotFoundError:
        print('The file, ', file_name, ', does not exist.')
    else:
        keyword = 'the '

        file_keyword_count = file_text.count(keyword)
    
        print("The number of times '", keyword, "' appeared in ", file_name, " is: ", file_keyword_count)
