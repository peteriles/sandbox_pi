# Exercises 10-11 ..
import json
from pathlib import Path

print('Exercise 10-11 and 10-12')

def get_stored_number(file_path_instance):
    """Retrieve number stored in a file"""
    
    # Check if the favourite number has already been stored
    if file_path_instance.exists():
        fave_number = file_path_instance.read_text()
    else:
        fave_number = None

    return fave_number


def prompt_for_number():
    """Prompt user for favourite number and return it"""
    request_loop_active = True

    while request_loop_active == True:
        fave_number = input("Tell me your favourite number: ")

        try:
            fave_number = int(fave_number) 
        except:
            print("Shoot! Your number is not an integer. Try again.")
        else:
            print("Number has been saved.")
            request_loop_active = False

    return fave_number


# Main routine

file_name = 'json_data.txt'
file_path_instance = Path(file_name)

# Check if the favourite number has already been stored
fave_number = get_stored_number(file_path_instance)

if fave_number:
    print('Saved info exists.')
    print("I know your favourite number, it's: ", fave_number)
else:
    print("Saved info does not exist. Querying user.")
    fave_number = prompt_for_number()

    # Store info in json format and write it to a file
    json_write_info = json.dumps(fave_number)
    file_path_instance.write_text(json_write_info)

print('\n')