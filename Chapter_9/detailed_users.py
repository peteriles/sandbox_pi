"""Module containing classes related to users"""
from users import User

class Privileges():
    """Privileges class"""

    def __init__(self, privileges):
        """Initialize attribute"""
        self.privileges = privileges

    def show_privileges(self):
        """Print the user's privileges"""

        print('The current privileges are:')
        for privilege in self.privileges:
            print(f'    Privilege: {privilege}')


class Admin(User):
    """Admin class which is a child of the User class"""

    def __init__(
            self, first_name, last_name, age, password, mother_maiden_name, 
            privileges):
        """
        Initialize attributes of the parent class.
        Then initialize attributes of the child class.
        """
        super().__init__(first_name, last_name, age, password, mother_maiden_name)

        # privileges attribute is an instance of class Privileges
        self.privileges = Privileges(privileges)