import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_name = entry.get()
    if user_name:
        messagebox.showinfo("Welcome!", f"Hello, {user_name}!")
    else:
        messagebox.showwarning("Try Again", "Please enter your name.")

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Create a text entry widget
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Submit", command=on_button_click, font=("Arial", 12))
button.pack(pady=20)

# Run the application
root.mainloop()
