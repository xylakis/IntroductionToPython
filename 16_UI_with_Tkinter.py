import tkinter as tk

def add_bread():
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, "Bread added!")
     
def add_patty():
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, "Patty added!")

def add_salad():
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, "Salad added!")



app_window = tk.Tk()
app_window.title('GUI App')

#In pixels
app_window.geometry('500x250')

label = tk.Label(app_window, text="Hello World!", font=('Arial', 18))
#specify layout 
label.pack(padx=20,pady=20)

#textbox 
textBox = tk.Text(app_window, height=2, font=('Arial', 16))
textBox.pack(padx=20)

button1 = tk.Button(app_window, width=10,text="Add Bread", command=add_bread)
button1.pack(pady=5)

button2 = tk.Button(app_window, width=10, text="Add Patty", command=add_patty)
button2.pack(pady=5)

button3 = tk.Button(app_window, width=10, text="Add Salad", command=add_salad)
button3.pack(pady=5)

textBox.insert(chars="Test",index="1.0")

app_window.mainloop()

