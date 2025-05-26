# We use conditionals tests to check if statements are TRUE or FALSE  

# cars = ["bmw","tesla","mazda","toyota","suzuki"]

#EQUALITY - INEQUALITY (==,!=)

# print(cars[0] == "bmw")
# print(cars[0] == "toyota")

#Lets check which one of the cars is a BMW

# input = 3

# if cars[input] == "bmw":
#     print("Its True the "+str(input)+" is a BMW")
# else:
#     print("Its False the",input," is not a BMW")

#If we want to check the opposite (if input is NOT EQUAL)

# print("The first car is NOT a bmw ",cars[0] != "bmw")
# print("The first car is NOT a toyota ",cars[0] != "toyota")

#NUMERICAL COMPARISONS (<,>,==,!=,>=,<=)

age = 16 
parent_rep = False
print(age<21)
print(age>21)
print(age==21)

#Multiple conditions checks (AND, OR) 
input_age = int(input("What's your age?"))

if input_age>16 and input_age<18:
    print("You can get a Scooter but not a car!")
elif input_age>=18 and input_age<=21:
    print("You can get your own car but not a Business Truck!")
elif input_age>21:
    print("Congrats, you get your own Business truck!")
else:
    print("You can't get anything... I am sorry, enjoy your bike.")

if input_age>=18 ^ parent_rep==True:
    print("You can have your Guardian get that car or you are of age")
else:
    print("No Guardian and no age limit, so no car.")

# #Check if Value is in List

# #EXAMPLE, is a car inside a list? 

# check_car = "Land rover"

# print("Is " + check_car + "inside the car list?", check_car in cars)
