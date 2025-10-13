from car import Car, EletricCar

my_audi = Car("audi", "a4", 2016)
print(my_audi.get_descriptive_name())
my_audi.odomter_reading = 23
my_audi.read_odometer()

my_tesla = EletricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()