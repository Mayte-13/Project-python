# Description
I want to create a book recommendation system.

First, the user will see a registration window where they need to register in the system 
(gender, name, age, favorite genres—this can be an optional field, password).

After that, the main page will open with a search bar (for author name, book title). 
Below the search bar, there will be genres that contain lists of all books from that genre and
recommendations from the app (such as the top 15 books in a specific genre).

The second page will be the user page, which will have sections:

1. This will show recommendations based on the user's personal data and genres chosen during registration. If the user didn't select genres during registration, 
this section will initially contain books that may be interesting based on their age. The user can add or remove genres at any time.
2. Read books.
3. Books saved for future reading.
4. Favorite books.
5. User's search history (this will provide recommendations based on their search history and books they viewed).
6. Recommendations based on the user's read books (this will provide books that are similar in genre and content to the books they've read).


# Functionality
1. User registration in the app.
2. Global search in the app by author name and book title.
3. Recommendations based on search history.
4. Recommendations based on read books.
5. Recommendations based on user data.


# Architecture
1.   class User: # This class represents a user and their data
         def __init__(self, username, gender, age = None, prefer_ganre = None ): // Initializes a user.
     Accepts arguments for username, password, age, gender, and preferred genres.


     Class attributes: 
         self.username = username # Stores the username.
         self.password = password # Stores the user's password
         self.age = age           # Stores the user's age
         self.gender = gender     # Stores the user's gender.
         self.prefer_ganre = prefer_ganre # Stores the user's gender.
         self.read_books = [] # Stores the books that the user has read.
         self.postponed_books = [] # Stores the books that the user has delayed (postponed)
         self.favorite_books = [] # Stores the user's favorite books.
         self.search_history = [] # Stores the user's search history.


         def add_genre(self, genre): # Method to add a genre.
         def delete_genre(self, genre): # Method to delete a genre.
         def add_to_read(self, book): # Method to add a book to the read list.
         def add_to_delay(self, book): # Method to add a book to the delayed (postponed) list.
         def add_to_favorites(self, book): # Method to add a book to the favorites list.
         def add_to_search_history(self, search_query): # Method to add a search query to the search history.


 2.  class Book: # This class represents a book and stores information about its title, author, and genres.
         def __init__(self, title, author, genres): # Initializes a book.
         Accepts arguments for the book title, author name, and genres


     Class attributes: 
         self.title = title # Stores the book title.
         self.author = author # Stores the author's name.
         self.genres = genres # Stores the book genres.

        def __repr__(self): # Returns a string in the format: "'Book Title' by Author".


 3. class BookRecommender: # This class manages book recommendations, including recommendations based on genres, read books, search history, and personal user data.
        def __init__(self, book_database): # Initializes an object of the BookRecommender class.       
        self.book_database = book_database # Stores the list of all available books in the system.

        def recommend_by_genres(self, user): # Stores the list of all available books in the system.
        user: User object.
        :return: A list of books.
       


        def recommend_by_age(self, user): # Recommends books based on the user's age.
        user: User object.
        :return: A list of books..


        def recommend_by_search_history(self, user): # Recommends books based on the user's search history.
        user: User object.
        :return: A list of books.

        def recommend_by_read_books(self, user): # Recommends books based on the books the user has read.
        user: User object.
        return: A list of books.


4.  class SearchEngine: # The SearchEngine class is designed to handle search queries for books by title or author.
        def __init__(self, book_database): # Initializes the class that is invoked when creating a new SearchEngine object.    
        attribute
        self.book_database = book_database # A list of all available books (objects of the Book class).

        def search(self, query): # This method searches for books by title or author based on the user's input query.
        query: Search string. # Accepts a query string from the user
        :return: A list of found books. # Returns a list of found books









