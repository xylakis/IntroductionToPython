#a list of words or strings 
my_string_list = ["souvlakia", "pizzes", "makaronades","burgerakia" ] 

#another list of integers
my_year_list = [2025, 1987, 2002, 2005]

#another list of floats 
class_heights = [1.81, 1.73, 1.71, 1.70, 1.83]

#names of the students
class_names = ["Papazoglou", "Statheas", "Mixeloudakis", "Marios", "Manolis"]

print("To megethos tis listas me ta ipsi einai:", len(class_heights))

for i in range(0, len(class_heights)):
    
    print(i)
    
    print("To ypsos tou " + str(class_names[i]) + " einai: " + str(class_heights[i]))

