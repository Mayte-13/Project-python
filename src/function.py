import tkinter as tk
from tkinter import messagebox
from user import User
from book import Book, book_data

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
    
    # Search button
    search_button = tk.Button(
        root,
        text="Search",
        font=("Arial", 14),
        command=lambda: search_books(search_entry.get(), root)
    )
    search_button.pack(pady=5)

    # Genres
    genres_label = tk.Label(main_root, text="Select a genre:", font=("Arial", 18), bg="#ffe590")
    genres_label.pack(pady=10)

    genres = list(book_data.keys())  
    for genre in genres:
        genre_button = tk.Button(main_root, text=genre, font=("Arial", 14),
                                 command=lambda g=genre: recommend_books(g, main_root))
        genre_button.pack(pady=5)

    main_root.mainloop()
    
# Book search
def search_books(query, window):
    """Searches for a book by title and displays the result."""
    global current_recommendations_label

    # Remove the current list of recommendations, if there is one.
    if current_recommendations_label:
        current_recommendations_label.destroy()

    # Searching for a book in the system
    found_books = []
    for genre, books in book_data.items():
        found_books.extend([book for book in books if query.lower() in book.title.lower()])

    # Forming a message with search results
    if found_books:
        recommendations = "\n\n".join([f"{book.title} by {book.author}" for book in found_books])
        result_text = f"Search results for '{query}':\n\n{recommendations}"
    else:
        result_text = f"No books found for '{query}'."

    # Display the results with larger font and spacing
    current_recommendations_label = tk.Label(
        window, 
        text=result_text, 
        font=("Arial", 16),  
        bg="#ffe590", 
        justify="left"
    )
    current_recommendations_label.pack(pady=20)

# Global variable to store the current list of recommendations
current_recommendations_label = None

def recommend_books(genre, window):
    """Recommends books by selected genre."""
    global current_recommendations_label

    # Delete the current list of recommendations if it exists
    if current_recommendations_label:
        current_recommendations_label.destroy()

    # We receive books according to the selected genre
    books = book_data.get(genre, [])
    recommendations = "\n\n".join([f"{book.title} by {book.author}" for book in books])
    
    # Displaying new recommendations with larger font and spacing
    current_recommendations_label = tk.Label(
        window, 
        text=f"Recommendations for '{genre}':\n\n{recommendations}", 
        font=("Arial", 16),  
        bg="#ffe590", 
        justify="left"
    )
    current_recommendations_label.pack(pady=20)
