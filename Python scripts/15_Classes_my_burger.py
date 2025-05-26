from my_burger_functions import add_a_patty, add_salad

class BurgerBuilder:
    
    def __init__(self):
        self.ingredients = []
        self.types_of_bread = ["(1) Whole wheat", "(2) Sesame bun", "(3) Brioche bread", "(4) Gluten free"]
        self.types_of_patty = ["(1) Beef", "(2) Fried chicken", "(3) Vegan"]
        self.type_of_salad  = ["(1) Lettuce", "(2) Coleslaw", "(3) Tomato"]

    def choose_bread(self):
        print("Please choose a type of bread from the list by typing the corresponding number ", self.types_of_bread)
        while True: 
            try: 
                bread = int(input("Bread number: "))
                if 0 < bread < 5:
                    print("You chose", self.types_of_bread[bread - 1])
                    self.ingredients.append(self.types_of_bread[bread - 1])
                    break
                else:
                    print("The number should be between 1 and 4.")
            except:
                print("Please provide an integer number between 1-4!")

    def add_patties(self):
        print("Please choose a type of patty from the list,", self.types_of_patty)
        add_a_patty(self.ingredients, self.types_of_patty)

        while input("Want to add another patty? (Yes/No) ").lower() == 'yes':
            add_a_patty(self.ingredients, self.types_of_patty)

    def add_salad(self):
        if input("Want some salad with this? (Yes/No) ").lower() == 'yes':
            print("Choose a type of salad from the list by typing the corresponding number", self.type_of_salad)
            add_salad(self.ingredients, self.type_of_salad)

    def remove_ingredient(self):
        if input("Want to remove something from your ingredients? (Yes/No) ").lower() == 'yes':
            to_remove = input("Type the ingredient you want to remove: ")
            while to_remove in self.ingredients:
                self.ingredients.remove(to_remove)

    def show_burger(self):
        print("Your final burger", self.ingredients)

# Example usage
burger = BurgerBuilder()
burger.choose_bread()
burger.add_patties()
burger.add_salad()
burger.remove_ingredient()
burger.show_burger()