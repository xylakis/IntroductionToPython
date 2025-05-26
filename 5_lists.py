
def delete_all(my_list,value_to_remove):

    while value_to_remove in my_list:
        my_list.remove(value_to_remove)

    return my_list

#1. create simple lists

fruits = ['apples','oranges','melons']

vehicles = ['mopeds','vespa', 'cross']

videogames = [2048, 'Last of us', 'Resident Evil 4']

#accessing elements and printing on screen 

print("My favourite game is " + str(videogames[0]))
#EXERCISE combine f-string to print list element with string

#2. Modifying elements of a list 

print("My favourite game is " + str(videogames[0]))

# simple at element at i 
videogames[0]='Sonic'

# adding an element to a list append (1 param value)
fruits.append('bananas')
print(fruits)

# addint an element to a list with insert (2 params, index and value)
fruits.insert(2,'apples')
print(fruits)

# removing element from a list with delete (1 param index)
fruits.remove('apples')
print(fruits)

# removing element from a list with pop, example with stacks
fruits.pop()
print(fruits)

# pop and save the popped item 
popped_fruit = fruits.pop()
print("Popped item", popped_fruit)
print(fruits)

# removing an element by name with remove multiple, custom function  
delete_all(fruits,'apples')

# sorting a list temporarily or permanently 
vehicles.sort()
print(vehicles)

# printing in reverse order as originally created 
vehicles.sort(reverse=True)
print(vehicles)

# sorting a list temporarily
# fruits is printed sorted but the 
# function does not change the list 
print(sorted(fruits))

# how do get the length of a list 
print(len(fruits))



