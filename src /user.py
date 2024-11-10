# Class to represent the user and their data
class User:
    def __init__(self, username, password, age=None, gender=None, prefer_genre=None):
        self.username = username         
        self.password = password            
        self.age = age                    
        self.gender = gender             
        self.prefer_genre = prefer_genre  
        self.read_books = []              
        self.postponed_books = []         
        self.favorite_books = []          
        self.search_history = [] 
                 
    # Method for adding genre
    def add_genre(self, genre):
        if genre not in self.prefer_genre:
            self.prefer_genre.append(genre)

    # Method to remove genre
    def delete_genre(self, genre):
        if genre in self.prefer_genre:
            self.prefer_genre.remove(genre)

   # Method to add a book to read
    def add_to_read(self, book):
        self.read_books.append(book)

   # Method for adding a book to the deferred
    def add_to_delay(self, book):
        self.postponed_books.append(book)


    # Method for adding a query to the search history
    def add_to_search_history(self, search_query):
        self.search_history.append(search_query)


