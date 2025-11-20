import string

prompt = "Please give me you Name and Surname: "

numbers = ['0','1','2','3','4','5','6','7','8','9'] 

# save all special chars so that we can check if the user has 
# entered their name correctly 
specials = set(string.punctuation)

# while the user inputs special chars within their name
# the following loops and keeps asking for input 
while True: 
    name = input(prompt)
    weird_char_detected = False

    for character in name:
        if character in numbers or character in specials:
            print("That is not your name")
            weird_char_detected = True
            # Ayth h Break spaei th for th loop 
            break

    if not weird_char_detected:
        print("That is your name ", name)
        #Ayth h break spaei th while 
        break

#Ensure that the input is integer
while True:
    age_prompt = name + (" Give me now your age: ")
    try:
        age = int(input(age_prompt))
        break
    except ValueError:
        print("Please provide an integer for your age " + name + " .")





        