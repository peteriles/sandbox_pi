# Exercise 11-3
class Employee:
    """Simple model of an employee"""
    def __init__(self, first_name, last_name, salary):
        """Initialize attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, raise_amount=5_000):
        """Give the employee a raise"""
        self.salary += raise_amount