import tkinter as tk
from tkinter import ttk
import pandas as pd 
from datetime import datetime as dt

def add_client():
    
    print(first_name.get(),surname.get(),
          device_var.get(),issue_text.get('1.0','end').strip(),
          resolved_var.get(),cost.get())
    
    #1. save the clients csv to a dataframe 
    df_clients = pd.read_csv("./Databases/my_clients.csv")

    current_date = dt.date(dt.now())

    if(resolved_var.get() == 1):
        resolved = 'True'
    else:
        resolved = 'False'
    
    #2. save all input fields to a new_client dataframe
    new_client = pd.DataFrame([{
        "Client Name": first_name.get(),
        "Client Surname": surname.get(),
        "Date": current_date,
        "Device": device_var.get(),
        "Issue": issue_text.get('1.0','end').strip(),
        "Resolved": resolved,
        "Charged Amount": cost.get()
    }])

    #3. Append or concat to the existing database (dataframe)
    df_clients = pd.concat([df_clients, new_client], ignore_index=True)

    #4. save the dataframe to our csv file
    df_clients.to_csv('Databases/my_clients.csv', index=False)

    first_name.delete(0, 'end')
    surname.delete(0, 'end')
    issue_text.delete(1.0, 'end')
    cost.delete(0,'end')

app_window = tk.Tk()

app_window.title('My Cool Clients registration App')

#In pixels
app_window.geometry('550x550')

input_frame = tk.Frame(app_window)
input_frame.pack(padx=10, pady=10)

# ---- First Name ----
tk.Label(input_frame, text="First Name:", font=('Arial', 14)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
first_name = tk.Entry(input_frame, font=('Arial', 14))
first_name.grid(row=0, column=1, padx=5, pady=5)

# ---- Last Name ----
tk.Label(input_frame, text="Last Name:", font=('Arial', 14)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
surname = tk.Entry(input_frame, font=('Arial', 14))
surname.grid(row=1, column=1, padx=5, pady=5)

# ---- Device dropdown ----
tk.Label(input_frame, text="Device:", font=('Arial', 14)).grid(row=2, column=0, sticky="w", padx=5, pady=5)

device_var = tk.StringVar()

device_dropdown = ttk.Combobox(
    input_frame,
    textvariable=device_var,
    font=('Arial', 14),
    state="readonly",
    values=[
        "Android",
        "Windows desktop",
        "Windows laptop",
        "Macbook",
        "iOS",
        "Linux laptop",
        "Smart TV",
        "Smartwatch"
    ]
)

device_dropdown.grid(row=2, column=1, padx=5, pady=5)
device_dropdown.current(5)  # default selection

# ---- Device Issue ---- 
tk.Label(input_frame, text="Issue:", font=('Arial', 14)).grid(row=3, column=0, sticky="w", padx=5, pady=5)

issue_text = tk.Text(
    input_frame,
    height=4,        # roughly 2 rows visually
    width=30,
    font=('Arial', 14),
    wrap="word"
)

issue_text.grid(
    row=3,
    column=1,
    rowspan=2,       # takes TWO grid rows
    sticky="w",
    padx=5,
    pady=5
)

# ---- Issue Resolved ----
tk.Label(input_frame, text="Resolved:", font=('Arial', 14))\
    .grid(row=5, column=0, sticky="w", padx=5, pady=5)

resolved_var = tk.BooleanVar(value=False)  # default

resolved_frame = tk.Frame(input_frame)
resolved_frame.grid(row=5, column=1, sticky="w", padx=5, pady=5)

tk.Radiobutton(
    resolved_frame,
    text="True",
    variable=resolved_var,
    value=True,
    font=('Arial', 14)
).pack(side=tk.LEFT)

tk.Radiobutton(
    resolved_frame,
    text="False",
    variable=resolved_var,
    value=False,
    font=('Arial', 14)
).pack(side=tk.LEFT)

# ---- Estimate Cost ----
tk.Label(input_frame, text="Estimate ($):", font=('Arial', 14))\
    .grid(row=6, column=0, sticky="w", padx=5, pady=5)

cost = tk.Entry(input_frame, font=('Arial', 14))
cost.grid(row=6, column=1, padx=5, pady=5)

myButton = tk.Button(input_frame , width=15, text="Add Client", font=('Arial', 14), command=add_client)
myButton.grid(row=7, column=0, pady=5)

app_window.mainloop()