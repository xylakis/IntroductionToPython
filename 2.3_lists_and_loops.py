#a list of words or strings 
my_streefood_list = ["souvlakia", "pizzes", "makaronades","burgerakia", "kebap", "kalamakia"] 

student_present_list = ["Giannis","Dimitris","Michalis"]

sudents_absent_list = ["Alban", "Maria"]

#another list of integers
my_year_list = [2025, 1987, 2002, 2005]

#another list of floats 
class_heights = [1.81, 1.73, 1.71, 1.70, 1.83]

#printing list elements 
print(my_streefood_list[0],my_streefood_list[2],my_streefood_list[4])

print("To megethos tis listas me ta streetfood einai:", len(my_streefood_list))

#Tupple examples, 
#converting a list to a tupple and vice versa
# tuple_example = ("souvlakia", "pizzes", "makaronades","burgerakia", "kebap", "kalamakia")   
# list_test = list(tuple_example)
# back_to_tupletuple=tuple(list_test)

# print(type(tuple_example))
# print(type(list_test))
# print(type(back_to_tupletuple))

# ---------------------- FOR LOOP ----------------------------------------------

# # 1st way to write a for loop 
# for i in range(0, len(my_streefood_list)):
#     print(i)
#     print(str(my_streefood_list[i]) + " is on the list" )

# # 2nd way to write a for loop 
# for student_present in student_present_list:
#     print(student_present)

# 3rd way to print a for loop with modulo operator %
# for i, street_food in enumerate(my_streefood_list):
#     # print(i,street_food)
#     if(i%2 != 0):
#         print(i,street_food)

# ---------------------- WHILE LOOP ----------------------------------------------
#1. While in normal order
i = 0

# A while loop runs until condition is FALSE
# while(i<len(my_streefood_list)):
#     print(my_streefood_list[i])
#     i += 1

#2. While in reverse order
# i = len(my_streefood_list) - 1

# A while loop runs until condition is FALSE
# while(i>=0):
#     print(i,my_streefood_list[i])
#     i -= 1

# name = input("What is your name? ")
# print(type(int(name)))
# print("Hello " + name + " welcome to the world of Python programming!")

#Combining a while loop with user input from the terminal
# while(input("I am at " + str(i) + " Tell me when to stop: ") != 'stop'):
    
#     if i >= len(my_streefood_list):
#         print("You have reached the end of the list")
#         break

#     print(my_streefood_list[i])
    
#     i += 1

#The opposite case
# while(input("I am at " + str(i) + " Tell me if I should go on: ") == 'go on'):
    
#     print(my_streefood_list[i])
    
#     i+=1

# ---------------------- LISTS ADVANCED ----------------------------------------------

# pushing an element to the end of the list with append() method
my_streefood_list.append("Curly fries")
print(my_streefood_list)

my_streefood_list.pop()
print(my_streefood_list)

my_streefood_list.pop()
print(my_streefood_list)

my_streefood_list.sort()
print(my_streefood_list)

my_streefood_list.append("souvlakia")
print(my_streefood_list)

my_streefood_list.append("souvlakia")
print(my_streefood_list)

print(my_streefood_list.count("souvlakia"))

# ---------------------- LISTS ADVANCED WITH LOOPS and INPUT ----------------------------------------------

my_order_list = []

while True:
    
    item = input("Give me order item or type stop")
    
    if(item =='stop'):
        break
    else:
        my_order_list.append(item)
        print(my_order_list)

print("Your order is ", my_order_list)












