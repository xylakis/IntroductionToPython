matrix = [[j for j in range(i, i + 6)] for i in range(1, 31, 6)]

my_matrix = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30]]


print("To stoixeio sth grammi 2 kai sth stili 4 einai to :" +str(matrix[2][4])) 

print("Ektypwsi ana grammi")
#Ektypwsi ana grammi
for x in range(0,5):
    for y in range(0,6):
        print(my_matrix[x][y])

print("Ektypwsi ana stili")
#Ektypwsi ana stili
for x in range(0,6):
    for y in range(0,5):
        print(my_matrix[y][x])