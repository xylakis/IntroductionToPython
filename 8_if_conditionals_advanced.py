#Example with if-elif-else 

age = int(input("What is your age? "))

if age < 4:
    print("Your admission cost is $0.")
elif age >= 4 and age < 18:
    print("Your admission cost is $15.")
elif age >= 18 and age < 25:
    print("Your admission cost is $20.")
elif age >= 25 and age < 65:
    print("Your admission cost is $40.")
else:
    print("Your admission cost is $5.")

# #if with Lists, making your pizza 

# current_pizza = ['dough','tomato_sauce']

# add_to_pizza = ['tomato_sauce', 'peppers', 'mushrooms', 'peperoni']

# for ingredient in add_to_pizza:

#     if ingredient in current_pizza:
#         print(ingredient + " is already in your pizza.")
#     else:
#         current_pizza.append(ingredient)
#         print(ingredient + " added to your pizza!")

# print("Your pizza has the following: ", current_pizza)

# For home burger maker. 
