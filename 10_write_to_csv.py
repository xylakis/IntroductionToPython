import csv
import pandas as pd
from datetime import datetime

df_clients = pd.read_csv("./Databases/Clients.csv")

#convert all date strings to Timestamps
df_clients["Date"] = pd.to_datetime(df_clients["Date"])

last_client_id = df_clients['Id_number'][len(df_clients['Id_number'])-1]

current_date = datetime.date(datetime.now())

# New record you want to add
new_row = {"Id_number":last_client_id+1, "Name": "Eleni", "Surname": "Drougka", "Date": current_date,
           "Device": "Phone", "Comments":" ", "Resolved": False}

# new_row.to_csv("customers.csv", mode="a", index=False, header=False)

# Recommended modern way
df_clients.loc[len(df_clients)] = new_row

# Save to CSV
df_clients.to_csv("./Databases/Clients.csv", index=False)

