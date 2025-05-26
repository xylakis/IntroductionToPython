# while True:
#     try:
#         user_input = int(input("Please provide an integer. "))
#         x = 5
#         print(x + user_input)
#     except:
#         print("Please use an integer")

array = [1,2,3,4]

try:
    for i in range(0,5):
        print(array[i]) 
except:
    print("You probably have exceeded the limit")

