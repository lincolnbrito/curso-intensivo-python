class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize the atrributes that describes a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odomer_reading = 0

    def get_descriptive_name(self):
        """Returns a descriptive name, formatted in ellegant way"""
        long_name = f"{str(self.year)} {self.make} {self.model}"
        
        return long_name.title()
    
    def read_odometer(self):
        """Displays a message showing the car's mileage."""
        print(f"The car has {str(self.odomer_reading)} miles on it.")

    def update_odometer(self, mileage):
        """Define an odometer's reading value
        Rejects the chage if the attempt is an update to set a lower value"""
        if mileage >= self.odomer_reading:
            self.odomer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        self.odomer_reading = mileage

    def increment_odometer(self, miles):
        """Sum the specified value to the odometer reading"""
        if miles > 0:
            self.odomer_reading += miles
        else:
            print("You can only increment the odometer reading with a value greater than zero")    

    
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying an attribute's directly
my_new_car.odomer_reading = 23
my_new_car.read_odometer()

# modifying an attribute's value using a method
my_new_car.update_odometer(34)
my_new_car.read_odometer()

# try to modify the odometer reading with a lower value
my_new_car.update_odometer(23500)

# increment the odometer reading
my_new_car.increment_odometer(10)
my_new_car.read_odometer()
my_new_car.increment_odometer(2000)
my_new_car.read_odometer()

# try to increment with a negative value
my_new_car.increment_odometer(-1)
my_new_car.increment_odometer(0)