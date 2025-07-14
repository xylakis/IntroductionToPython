import tkinter as tk
from MyBurgerClass import BurgerBuild

def add_bread_sesame():
     
     burger.add_bread_sesame()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)
     
def add_bread_whole():
     
     burger.add_bread_whole()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_bread_sweet():
     
     burger.add_bread_sweet()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_patty_beef():
     
     burger.add_patty_beef()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_patty_chicken():
     
     burger.add_patty_chicken()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_patty_vegan():
     
     burger.add_patty_vegan()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def remove_all_patties():
     burger.remove_all_patties()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_salad_lettuce():
     burger.add_salad_lettuce()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_salad_coleslaw():
     burger.add_salad_coleslaw()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def add_salad_tomato():
     burger.add_salad_tomato()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)

def remove_all_salad():
     burger.remove_all_salad()
     textBox.delete('1.0', tk.END)
     textBox.insert(tk.END, burger.ingredients)


burger = BurgerBuild()

app_window = tk.Tk()
app_window.title('GUI App')

#In pixels
app_window.geometry('700x300')

label = tk.Label(app_window, text="Welcome to my Burger Builder App!", font=('Arial', 18))
#specify layout 
label.pack(padx=20,pady=20)

#textbox 
textBox = tk.Text(app_window, height=4, font=('Arial', 16))
textBox.pack(padx=20)

# Control variable for the radio buttons
var = tk.IntVar()

# Create a frame for horizontal layout
radio_frame = tk.Frame(app_window)
radio_frame.pack(pady=5)

# Create radio buttons
radio1 = tk.Radiobutton(radio_frame, text="Sesame bun", variable=var, value=1, command=add_bread_sesame)
radio1.pack(side=tk.LEFT, padx=5)

radio2 = tk.Radiobutton(radio_frame, text="Whole wheat", variable=var, value=2, command=add_bread_whole)
radio2.pack(side=tk.LEFT, padx=5)

radio3 = tk.Radiobutton(radio_frame, text="Sweet bun", variable=var, value=3, command=add_bread_sweet)
radio3.pack(side=tk.LEFT, padx=5)

# Create a frame to hold the buttons horizontally
button_frame_patty = tk.Frame(app_window)
button_frame_patty.pack(pady=5)

button1a = tk.Button(button_frame_patty, width=20,text="Beef", command=add_patty_beef)
button1a.pack(side=tk.LEFT,pady=10)

button1b = tk.Button(button_frame_patty, width=20,text="Chicken", command=add_patty_chicken)
button1b.pack(side=tk.LEFT,pady=10)

button1c = tk.Button(button_frame_patty, width=20,text="Vegan", command=add_patty_vegan)
button1c.pack(side=tk.LEFT,pady=10)

button2None = tk.Button(button_frame_patty, width=10,text="Remove", command=remove_all_patties)
button2None.pack(side=tk.LEFT,pady=10)

button_frame_salad = tk.Frame(app_window)
button_frame_salad.pack(pady=5)

button2a = tk.Button(button_frame_salad, width=20,text="Lettuce", command=add_salad_lettuce)
button2a.pack(side=tk.LEFT,pady=10)

button2b = tk.Button(button_frame_salad, width=20,text="Coleslaw", command=add_salad_coleslaw)
button2b.pack(side=tk.LEFT,pady=10)

button2c = tk.Button(button_frame_salad, width=20,text="Tomato", command=add_salad_tomato)
button2c.pack(side=tk.LEFT,pady=10)

button2None = tk.Button(button_frame_salad, width=10,text="Remove", command=remove_all_salad)
button2None.pack(side=tk.LEFT,pady=10)

app_window.mainloop()

