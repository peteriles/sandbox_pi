"""Module containing a class related to users"""

class User:
    """Simple model of a user"""

    def __init__(self, first_name, last_name, age, password, mother_maiden_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.mother_maiden_name = mother_maiden_name
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information"""
        full_name = f'{self.first_name.title()} {self.last_name.title()}'

        print(f'Info on user: {full_name}')
        print(f'    First name: {self.first_name.title()}')
        print(f'    Last name: {self.last_name.title()}')
        print(f'    Age: {self.age}')
        print(f'    Password: {self.password}')
        print(f"    Mother's maiden name: {self.mother_maiden_name}")
        print('\n')
        

    def greet_user(self):
        """Print a message greeting the user"""
        print(f'Well, hello there, {self.first_name.title()}!')
        print('\n')

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0
