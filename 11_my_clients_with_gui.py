import tkinter as tk

def add_bread():
    app_window_B = tk.Tk()
    app_window_B.title('My Cool Clients B')
    app_window_B.geometry('1000x500')
    app_window_B.mainloop()

def choose_android():
    print("Test")

app_window = tk.Tk()
#app_window_B = tk.Tk()

print(type(app_window))

app_window.title('My Cool Clients registration App')
#app_window_B.title('My Cool Clients B')

#In pixels
app_window.geometry('1000x250')


myButton = tk.Button(app_window, width=10 ,text="Add Client", command=add_bread)
myButton.pack(pady=5)

#textbox 
textBox = tk.Text(app_window, height=2, font=('Arial', 16))
textBox.pack(padx=20)

# label = tk.Label(app_window, text="Choose Device", font=('Arial', 18))
# #specify layout 
# label.pack(padx=20,pady=20)

# Create a frame for horizontal layout
radio_frame = tk.Frame(app_window)
radio_frame.pack(pady=5)

# Control variable for the radio buttons
var = tk.IntVar()

label = tk.Label(radio_frame, text="Choose Device", font=('Arial', 14))
#specify layout 
label.pack(side=tk.LEFT,padx=0)

# Create radio buttons
radio1 = tk.Radiobutton(radio_frame, text="Android", variable=var, value=1, command=choose_android)
radio1.pack(side=tk.LEFT, padx=55)

radio2 = tk.Radiobutton(radio_frame, text="Windows desktop", variable=var, value=2, command=choose_android)
radio2.pack(side=tk.LEFT, padx=5)

radio3 = tk.Radiobutton(radio_frame, text="Windows laptop", variable=var, value=3, command=choose_android)
radio3.pack(side=tk.LEFT, padx=5)

radio4 = tk.Radiobutton(radio_frame, text="Macbook", variable=var, value=4, command=choose_android)
radio4.pack(side=tk.LEFT, padx=5)

radio5 = tk.Radiobutton(radio_frame, text="iOS", variable=var, value=5, command=choose_android)
radio5.pack(side=tk.LEFT, padx=5)

radio6 = tk.Radiobutton(radio_frame, text="Linux Laptop", variable=var, value=6, command=choose_android)
radio6.pack(side=tk.LEFT, padx=5)

radio7 = tk.Radiobutton(radio_frame, text="Smart TV", variable=var, value=7, command=choose_android)
radio7.pack(side=tk.LEFT, padx=5)

radio8 = tk.Radiobutton(radio_frame, text="Smartwatch", variable=var, value=8, command=choose_android)
radio8.pack(side=tk.LEFT, padx=5)

# appWindow.title("My First Tkinter App")
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack(padx=20, pady=20)

app_window.mainloop()


