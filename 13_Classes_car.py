class Car:
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # We can set a default value for the attributes 
        # without explicitly asking for it 
        self.odometer_reading = 0
        self.gas_tank = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def update_odometer_improved(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def get_gas_tank(self):
        return self.gas_tank

    def fill_gas_tank(self,liters):
        """Cars do have gas tanks though!"""
        self.gas_tank += liters
        print(f"This car has currently {self.gas_tank} litters!")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40
        # self.battery_size = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
        

my_new_car = Car('Audi', 'a4', 2024)
my_second_car = Car('Opel','Corsa', 1998)

print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
print(my_second_car.read_odometer())

my_second_car.update_odometer_improved(10000)

print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
print(my_second_car.get_descriptive_name())
print(my_second_car.read_odometer())

my_second_car.update_odometer_improved(5000)

print(my_second_car.get_descriptive_name())
print(my_second_car.read_odometer())

# my_new_car.read_odometer()
# my_new_car.fill_gas_tank(30)
# my_new_car.fill_gas_tank(40)

# print(my_new_car.get_gas_tank())