class BurgerBuild:
    
    def __init__(self):
        self.ingredients = []
        self.types_of_bread = ["Top Sesame","Bottom Sesame","Top Whole", "Bottom Whole", "Top Sweet", "Bottom Sweet"]
        self.types_of_patty = ["Beef", "Chicken", "Vegan"]
        self.type_of_salad  = ["Lettuce", "Coleslaw", "Tomato"] 

    def add_bread_sesame(self):

        if any(bread in self.ingredients for bread in self.types_of_bread):
            self.ingredients = []
        self.ingredients.append("Top Sesame")
        self.ingredients.append("Bottom Sesame")

    def add_bread_whole(self):

        if any(bread in self.ingredients for bread in self.types_of_bread):
            self.ingredients = []
        self.ingredients.append("Top Whole")
        self.ingredients.append("Bottom Whole")     

    def add_bread_sweet(self):

        if any(bread in self.ingredients for bread in self.types_of_bread):
            self.ingredients = []
        self.ingredients.append("Top Sweet")
        self.ingredients.append("Bottom Sweet") 

    def add_patty_beef(self):
        self.ingredients.insert(-1,"Beef")
    
    def add_patty_chicken(self):
        self.ingredients.insert(-1,"Chicken")
    
    def add_patty_vegan(self):
        self.ingredients.insert(-1,"Vegan")

    def remove_all_patties(self):
        i = 0
        while i < len(self.ingredients):
            if self.ingredients[i] in self.types_of_patty:
                self.ingredients.pop(i)
            else:
                i += 1

    def add_salad_lettuce(self):
        self.ingredients.insert(-1,"Lettuce")
    
    def add_salad_coleslaw(self):
        self.ingredients.insert(-1,"Coleslaw")
    
    def add_salad_tomato(self):
        self.ingredients.insert(-1,"Tomato")

    def remove_all_salad(self):
        i = 0
        while i < len(self.ingredients):
            if self.ingredients[i] in self.type_of_salad:
                self.ingredients.pop(i)
            else:
                i += 1



    