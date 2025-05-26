
def add_a_patty(ingredients,types_of_patty):
    while True: 
        try: 
            patty = int(input("Patty number: "))
            if(patty<4 and patty>0):
                print("You choose ", types_of_patty[patty-1])
                ingredients.append(types_of_patty[patty-1])
                break
            else:
                print("Please enter a number between 1 and 3.")
        except:
            print("Please provide a number between 1-3")

def add_salad(ingredients, type_of_salad):
    while True: 
        try: 
            salad = int(input("Salad number: "))
            if(salad<4 and salad>0):
                print("You choose ", type_of_salad[salad-1])
                ingredients.append(type_of_salad[salad-1])
                break
            else:
                print("Please enter a number between 1 and 3.")
        except:
            print("Please provide a number between 1-3")