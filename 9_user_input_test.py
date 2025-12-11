from datetime import datetime as dt

devices_list = ['(1) Android','(2) Windows desktop', '(3) Windows laptop', '(4) Macbook', '(5) iOS', '(6) Linux laptop', '(7) Smart TV', 
                '(8) Smartwatch']

print("Welcome to my Amazing IT Support Store.")

client_name = input("Enter your Name: ")

client_surname = input("Enter your Surname: ")

print("Hello ", client_surname,client_name)

current_date = dt.date(dt.now())

print("Choose device type by inputing the corresponding number: ")

while True:
    try:
        #get input from the user and change it 
        device_nr = int(input(devices_list))
        break
    except ValueError:
        print("Please provide an integer for a number.!!!!!!")

device_nr = int(device_nr)

device = devices_list[device_nr-1]

print("You have chosen ", device)

device_issues = input("What is the issue with your device? ")

print("Test")

while True:
    try:
        resolved = int(input("Has this issue been resolved? press (1)['True'] or (2)['False']: "))
        #Check this
        # if resolved >= 2:
        #     raise ValueError("Number must be less than 2")

        break
    except ValueError:
        print("You must choose either (1) or (2)")

charged_amount = input("What is the estimate charge ?")

charged_amount = float(charged_amount)

new_client = pd.DataFrame([{
    "Client Name": client_name,
    "Client Surname": client_surname,
    "Date": current_date,
    "Device": device,
    "Issue": device_issues,
    "Resolved": resolved,
    "Charged Amount": charged_amount
}])
    

