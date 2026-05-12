import eight_defs

# #function no input no return, just print
# def age_restrictions():
    
#     age = int(input("What is your age? "))

#     if age < 4:
#         print("Your admission cost is $0.")
#     elif age >= 4 and age < 18:
#         print("Your admission cost is $15.")
#     elif age >= 18 and age < 25:
#         print("Your admission cost is $20.")
#     elif age >= 25 and age < 65:
#         print("Your admission cost is $40.")
#     else:
#         print("Your admission cost is $5.")

# # age_restrictions()

# #function that accepts input 
# # 
# def count_up_until(number): 
    
#     number = int(number)

#     for i in range(0,number):
#         print(i) 

# count_up_until(input("Give me a number to count up until "))

# def calculator(number_a,number_b,operation):

#     if (operation == '+'):
#         return number_a + number_b
#     elif (operation == '-'):
#         return number_a - number_b
#     elif (operation == '*'):
#         return number_a * number_b
#     elif (operation == '/'):
#         if (number_b == 0):
#             print("number_b cannot be 0")
#         else: 
#             return number_a / number_b
#     else :
#         print("Does not support this opperation, use +,-,/,*")


# print(calculator(5,18,'/'))


fpa = 0.24 

european_country = input("Which country are you in?")

fpa = eight_defs.adjust_vat_eu(european_country)

print("Your fpa is ", fpa)





# item_price = input("give me the price of the requested item")

# print("This is the total cost incl vat", item_price*fpa + item_price)



