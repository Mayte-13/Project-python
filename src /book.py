class Book:
    
    def __init__(self, title, author, genres):
        self.title = title
        self.author = author
        self.genres = genres

    def __repr__(self):
        return f"'{self.title}' by {self.author}"