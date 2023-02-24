"""Module containing the Restaurant class """

class Restaurant:
    """A simiple model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize instance of class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Set the value of attribute number_served"""
        self.number_served = number_served

    def increment_number_served(self, num_served_increment):
        """Increment the number of people served"""
        self.number_served += num_served_increment