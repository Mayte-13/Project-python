import tkinter as tk
from tkinter import messagebox
import function
        
# Setting up a tkinter window
root = tk.Tk()
root.title("Book Recommendation System - Registration")
root.geometry("400x400")
root.configure(bg="#ffe590") 
 

# Welcome message
welcome_label = tk.Label(
    root,
    text="Welcome to the book recommendation system!\nPlease register in our system",
    font=("Arial", 24), 
    bg="#ffe590",
    fg="green",
    pady=20
)
welcome_label.pack()

# Registration fields
tk.Label(root, text="Name", font=("Arial", 18),bg="#ffe590" ).pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Gender: please enter W/M", font=("Arial", 18), bg="#ffe590").pack()
gender_entry = tk.Entry(root)
gender_entry.pack()

tk.Label(root, text="Age", font=("Arial", 18), bg="#ffe590").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Favorite Genres (optional)", font=("Arial", 18), bg="#ffe590").pack()
genres_entry = tk.Entry(root)
genres_entry.pack()

tk.Label(root, text="Password", font=("Arial", 18), bg="#ffe590").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Registration button
register_button = tk.Button(root, text="Register", 
                            font=("Arial", 18), bg="#ffe590", fg="red",
                            command=lambda: function.register_user(
                                root,
                                name_entry.get(),
                                password_entry.get(),
                                age_entry.get(),
                                gender_entry.get(),
                                genres_entry.get().split(",") if genres_entry.get() else []
                            ))
register_button.pack()

root.mainloop()

