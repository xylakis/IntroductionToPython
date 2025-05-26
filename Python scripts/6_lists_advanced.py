# STRING LISTS 
favourite_beers_ranked = ['Xarma', 'Kaiser', 'Alpha', 'Fisher', 'Amstel', 'Mamos']

print("My ranked list of beers!")

#The for loop goes through all the beers in the list 
for beer in favourite_beers_ranked:
    print(beer)

#Enumerate return both the value of the list and its index on the array 
#so I can either choose index or value depending on my program

for b,beer in enumerate(favourite_beers_ranked):
    print(b,beer)

#Indentetion is an Important aspect of a loop, indicating what
#is part of the loop and repeats and what stays outside and runs 
#regardless of the loop. 

print("Printed all beers, Thank you!")

# NUMBERICAL LISTS
list_a = [75, 8, 19, 8, 3]

#create an incremental list with the range() function 
list_incremental = list(range(1,6))

print(list_a[2])

#print all numbers using len 
for value in range(0,len(list_incremental)):
    print(value)

#Controling my for loop: start, stop and step
for i in range(0,5,1):
    print(list_a[i])

#EXERCISE: Creating a list using append(), range() and a for loop
myList = []

for i in range(0,10):
    value = i*5
    myList.append(value)

print(myList)

#List statistics, metrics MAX(), MIN(), SUM()

print("The maximum of my list is:", max(myList))
print("The minimum of my list is:", min(myList))
print("The sum of my list is:", sum(myList))


 
 