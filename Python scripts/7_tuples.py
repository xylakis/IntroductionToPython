#We use lists to store data that could change throughout the lifecycle 
#of a program

# Tuples are a special kind of list that does not support changes (immutable). 
# When creting a tuple we use parentheses () rather than brackets []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (150,50)

# What happens if I try and change one of its values? 
#dimensions[0]=250

#supports regular functions as a list 
print(len(dimensions))

#if in any case we want to change its value throughout a program
#the tuple has to be redefined from scratch 

print("Tuple before change", dimensions)

dimensions = (140,20)

print("Tuple after change", dimensions)
