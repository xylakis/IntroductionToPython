#Input by user is interpreted in Python as a string
# message = input("Hey, what is you name?")

# print("Hello "+str(message)+" !")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(name)

#What if I want an input that is not a string and its an int?
another_prompt = "How old are you then " + name + " ? "

while True:
    try:
        age = int(input(another_prompt))
        break
    except ValueError:
        print("Please provide an intiger for your age " + name + " .")

# while(type(age)!= int):
#     age = input("I need a intiger numerical value for your age ", name)