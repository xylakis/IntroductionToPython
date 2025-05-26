#Example with if-elif-else 

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#if with Lists, making your pizza 

current_pizza = ['dough','tomato_sauce']

add_to_pizza = ['tomato_sauce', 'peppers', 'mushrooms', 'peperoni']

for ingredient in add_to_pizza:

    if ingredient in current_pizza:
        print(ingredient + " is already in your pizza.")
    else:
        current_pizza.append(ingredient)
        print(ingredient + " added to your pizza!")

print("Your pizza has the following: ", current_pizza)

# For home burger maker. 
