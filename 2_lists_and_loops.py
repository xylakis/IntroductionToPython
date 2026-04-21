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

# ---------------------- FOR LOOP ----------------------------------------------

# 1. way to write a for loop 
# for i in range(0, len(my_streefood_list)):
#     print(i)
#     print(str(my_streefood_list[i]) + " is on the list" )

# 2nd way to write a for loop 
# for student_present in student_present_list:
#     print(student_present)

# 3rd way to print a for loop with modulo operator %
# for i, student_present in enumerate(student_present_list):
#     if(i%2 == 0):
#         print(i,student_present)

# ---------------------- WHILE LOOP ----------------------------------------------

i = 0

# A while loop runs until condition is FALSE
# while(i<len(student_present_list)):
#     print(student_present_list[i])
#     i -= 1

#Combining a while loop with user input from the terminal
# while(input("I am at " + str(i) + " Tell me when to stop: ") != 'stop'):
    
#     print(my_streefood_list[i])
    
#     i+=1

#The opposite case
# while(input("I am at " + str(i) + " Tell me if I should go on: ") == 'go on'):
    
#     print(my_streefood_list[i])
    
#     i+=1

# ---------------------- LISTS ADVANCED ----------------------------------------------

#Adding new elements to a list

# my_streefood_list.append("Curly fries")
# print(my_streefood_list)

# my_streefood_list.pop()
# print(my_streefood_list)

# my_streefood_list.pop()
# print(my_streefood_list)

# my_streefood_list.sort()
# print(my_streefood_list)

# my_streefood_list.append("souvlakia")
# print(my_streefood_list)

# print(my_streefood_list.count("souvlakia"))

# ---------------------- LISTS ADVANCED WITH LOOPS----------------------------------------------

while(input("Tell me if I should go on: ") == 'go'):

    item = input("Give me a streetfood to add to the list: ")
    
    my_streefood_list.append(item)
    
    print(my_streefood_list)

while True:
    item = input("Give me order item or type stop")
    if(item =='stop'):
        break
    else:
        my_streefood_list.append(item)
        print(my_streefood_list)
print("Your order is ", my_streefood_list)












