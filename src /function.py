import tkinter as tk
from tkinter import messagebox
from user import User
from book import Book


# User registration window
def register_user(root, username='', password='', age = 0, gender ="", prefer_genre = []):
    if password == '' or username == '':
        pass
    else:
        user = User(username, password, age, gender, prefer_genre)
        messagebox.showinfo("Registration Successful", f"Welcome, {user.username}!")
        # Close the registration window
        root.destroy()

        # Open the main window
        open_main_page(user)
        
        
 # Home page   
def open_main_page(user):
    """Opens the main window with a search bar and genres."""
    root = tk.Tk()
    main_root = root
    main_root.title("Main Page - Book Recommendations")
    main_root.geometry("600x600")
    main_root.configure(bg="#ffe590")

    # Welcome message
    welcome_label = tk.Label(
        main_root,
        text=f"Welcome {user.username}!\nSearch for books and select genres.",
        font=("Arial", 20),
        bg="#ffe590",
        fg="green",
        pady=20
    )
    welcome_label.pack()

   # Book search field
    search_label = tk.Label(main_root, text="Search books:", font=("Arial", 18), bg="#ffe590")
    search_label.pack(pady=10)

    search_entry = tk.Entry(main_root, font=("Arial", 14))
    search_entry.pack(pady=10)

    # Genres
    genres_label = tk.Label(main_root, text="Select a genre:", font=("Arial", 18), bg="#ffe590")
    genres_label.pack(pady=10)

    genres = ["World Classics", "Detectives", "Fantasy", "Psychology"]
    for genre in genres:
        genre_button = tk.Button(main_root, text=genre, font=("Arial", 14), command=lambda g=genre: recommend_books(g, main_root))
        genre_button.pack(pady=5)

    main_root.mainloop()
    
    
    
book_data = {
    "World Classics": [
        Book("1984", "George Orwell", ),
        Book("Brave New World", "Aldous Huxley ", ),
        Book("Life on Loan", "Remarque Erich Maria ", ),
        Book("The Art of Loving", "Erich Fromm ", ),
        Book("Arc de Triomphe", "Erich Maria Remarque", ),
        Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", ),
        Book("Pride and Prejudice", "Jane Austen", ),
        Book("Lord of the Flies", "William Golding ", ),
        Book("The Hitchhiker's Guide to the Galaxy. The Restaurant at the End of the Universe", "Douglas Adams", ),
        Book("To Kill a Mockingbird", "Harper Lee", ),
        Book("A Clockwork Orange", "Burgess Anthony", ),
        Book("The Picture of Dorian Gray", "Oscar Wilde", ),
        Book("Letters to a Stranger", "Maurois Andre ", ),
        Book("The Man Who Mistook His Wife for a Hat and Other Medical Stories", "Sacks Oliver ", ),
        Book("Animal Farm. Essay", "Orwell George ", ),
        Book("The Notebook", "Sparks Nicholas", ),
        Book("Night in Lisbon", "Remarque Erich Maria ", ),
        Book("All Quiet on the Western Front", "Remarque Erich Maria",),
        Book("Fight Club", "Chuck Palahniuk", ),
        Book("Three Comrades", "Remarque Erich Maria", )
    ],
    # Additional genres can be added here
}


# Global variable to store the current list of recommendations
current_recommendations_label = None

def recommend_books(genre, window):
    """Recommends books by selected genre"""
    global current_recommendations_label

    # Delete the current list of recommendations if it exists
    if current_recommendations_label:
        current_recommendations_label.destroy()

    # We receive books according to the selected genre
    books = book_data.get(genre, [])
    recommendations = "\n\n".join([f"{book.title} by {book.author}" for book in books])

    # Displaying new recommendations
    current_recommendations_label = tk.Label(window, text=f"Recommendations for '{genre}':\n\n{recommendations}", font=("Arial", 14), bg="#ffe590", justify="left")
    current_recommendations_label.pack(pady=10)
       
        