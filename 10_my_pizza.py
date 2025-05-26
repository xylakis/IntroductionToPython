incredients_in_my_pizza = ['dough']

print("Make your own pizza by typing all the ingredients that you want.")

ingredient = input("Add ingredient: ")

while (ingredient!='Stop'):

    if (ingredient not in incredients_in_my_pizza):
        print("Add another ingredient please.")
        incredients_in_my_pizza.append(ingredient)

    ingredient = input("Add ingredient: ")

print("Current pizza setup ",incredients_in_my_pizza)
