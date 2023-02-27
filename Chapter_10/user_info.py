# Exercise 10-13 and 10-14
print('Exercise 10-13')

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Prompt for info about a new user and write it to a file."""
    user_dict = {}
    user_dict['username'] = input("What is your name? ")
    user_dict['user_age'] = input("What is your age? ")
    user_dict['user_height'] = input("What is your height? ")
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name and report all known user info."""
    path = Path('user_info.json')
    user_info = get_stored_username(path)

    if user_info:
        # Ask user if the stored username is, in fact, them
        response = input(f"Hello, are you {user_info['username']}? (y/n) ")

        if response == "y":
            print(f"Welcome back, {user_info['username']}!")
            print(f"You are {user_info['user_age']} years old.")
            print(f"You are {user_info['user_height']} inches tall.")
        else:
            print("OK, we'll just need a bit of info, then.")
            get_new_user_info(path)
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")


greet_user()