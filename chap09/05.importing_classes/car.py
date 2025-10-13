"""A set of classes used to represent gasoline and eletric cars"""
class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize the car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns the descriptive name formated in elegant way"""
        long_name = f"{str(self.year)} {self.make} {self.model}"

        return long_name.title()
    
    def read_odometer(self):
        """Show a message informing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles out.")

    def update_odometer(self, mileage):
        """Define the odometer reading with specified value"""
        """Rejects the change if the informed is lower than odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Sum the specified quantity with odometer readin"""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to represent a battery for an eletric car"""
    def __init__(self, battery_size=60):
        """Initialize the battery attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Show a message describing the battery capacity"""
        print(f"This car has a {str(self.battery_size)}-kWh battery.")

    def get_range(self):
        """Show a message informing the distance that car can make with this battery."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f"This car can go approximately {str(range)} miles on a full charge."

        print(message)

class EletricCar(Car):
    """Model specific aspects of an eletric car"""
    def __init__(self, make, model, year):
        """
        Initialize the super class atrributes
        Then initialize the specific attributes of an eletric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()