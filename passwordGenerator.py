import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Function to generate a random password
def generate_random_password(length):
    password = ""
    for i in range(0,length):
        options = [letters,numbers,symbols]
        random_options = random.choice(options)
        password += random.choice(random_options)

    return password

# Function to show the pop-up and generate the password
def show_popup():
    length = simpledialog.askinteger("Input", "How long do you want the password to be?", minvalue=1, maxvalue=128)
    if length:
        password = generate_random_password(length)
        messagebox.showinfo("Generated Password", f"Your password is: {password}")

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# Create a button to trigger the pop-up
button = tk.Button(root, text="Generate a Password", command=show_popup)
button.pack(pady=20)

# Run the application
root.mainloop()
