# Excercise 9-9

class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        unknown_battery_flag = False

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            print("Unknown battery type!")
            unknown_battery_flag = True

        if not unknown_battery_flag:
            print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        """
        Check the battery size and set capacity to 65kWH if not already 
        at that value
        """
        if self.battery_size == 65:
            print('Battery is already upgraded to 65kwH')
        else:
            print('Upgrading battery to 65kWh!')
            self.battery_size = 65


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()