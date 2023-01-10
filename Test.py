import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello, World")
window.geometry("800x600")
## defienes the variable hello
def hello(): 
    print("Hello, World")
# Create a button that says "Click me"
button = tk.Button(text="Click me", command=hello)
button.pack()

# Create a function that will be called when the button is clicked
def hello():
    print("Welcome to the world of programming")

# Run the Tkinter event loop
window.mainloop()
