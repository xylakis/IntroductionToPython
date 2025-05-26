class Dog:
    """A simple attempt to model a dog."""
    
    # A function that’s part of a class is also called a method.
    # The __init__ methods run automatically whenever we create a
    # new instance based on the Dog class. 
    def __init__(self, name, age, food):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.food = food
    
    # The 1st method of my dog class
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    # The 2nd method of my dog class 
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def eat(self, food):
        print(f"{self.name} is eating  {food}!")

my_dog = Dog('Wille',6,"Stake")

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"My dog is eating a {my_dog.food}")