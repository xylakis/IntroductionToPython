from my_burger_functions import add_a_patty,add_salad 

ingredients = []

types_of_bread = ["(1) Whole wheat", "(2) Sesame bun", "(3) Brioche bread", "(4) Glutten free"]
types_of_patty = ["(1) Beef", "(2) Fried chicken", "(3) Vegan"]
type_of_salad  = ["(1) Lettuce", "(2) Coleslaw", "(3) Tomato"]

print("Please choose a type of bread from the list by typing the corresponding number ", types_of_bread)

#1. Get the bread 
while True: 
    try: 
        bread = int(input("Bread number: "))
        if(bread<5 and bread>0):
            print("You choose ", types_of_bread[bread-1])
            ingredients.append(types_of_bread[bread-1])
            break
        else:
            print("The number should be between 1 and 4.")
    except:
        print("Please provide an intiger number between 1-4!")

#2. Get the patty 
print("Please choose a type of patty from the list, ", types_of_patty)
add_a_patty(ingredients,types_of_patty)

extra_patty_check = input("Want to add another patty? (Yes/No) ")

while(extra_patty_check == 'Yes' or extra_patty_check == 'yes'):
    add_a_patty(ingredients,types_of_patty)
    extra_patty_check = input("Want to add another patty? (Yes/No) ")

#3. Add salad 
salad_check = input("Want some salad with this ? (Yes/No) ")
if (salad_check == "Yes"):
    print("Choose a type of salad from the list by typing the corresponding number ", type_of_salad)
    add_salad(ingredients,type_of_salad)
    print("Your final burger ", ingredients)
else: 
    print("Your final burger ", ingredients)

#4. Removing something from the list 
remove_check = input("Want to remove something from your ingredients ? (Yes/No) ")

if (remove_check == "Yes"):
    ingredient_to_remove = input("Type the ingredient you want to remove: ")

    while(ingredient_to_remove in ingredients):
        ingredients.remove(ingredient_to_remove)

    print("Your final burger ", ingredients)
else: 
    print("Your final burger ", ingredients)
