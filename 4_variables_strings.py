#simple strings 

message = "Hello world in Python from variable"

print(message)

my_name = "Manolis"
my_surname = "Xylakis"

age = 37 

#Common functions when working with strings 

test_string = "            the origin of species "

print("This is a Title format:" + test_string.title())
print("This is a lower case example:" + test_string.lower())
print("This is an upper/CAPS case example:" +test_string.upper())

# #f-strings 
full_name = f"{my_name} {my_surname}"

# #printing stings with variables
print(f"Hello, {full_name} !")
print("Hello " + str(age) + "!")

# #strip 
print("This is an upper case example:"+test_string.strip())


# #printing quotes
famous_quotes_oscar = ' “Be yourself; everyone else is already taken.”― Oscar Wilde '

print(famous_quotes_oscar)


