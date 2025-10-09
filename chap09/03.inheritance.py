class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"The car has {str(self.odomer_reading)} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odomer_reading:
            self.odomer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        self.odomer_reading = mileage

    def increment_odometer(self, miles):
        if miles > 0:
            self.odomer_reading += miles
        else:
            print("You can only increment the odometer reading with a value greater than zero")    

class EletricCar(Car):
    """Represents specific aspects of eletric cars"""
    def __init__(self, make, model, year):
        """Initialize super class attributes"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Show a message describing the battery's capacity"""
        print(f"This car has a {str(self.battery_size)}-kWh battery")


my_tesla = EletricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()