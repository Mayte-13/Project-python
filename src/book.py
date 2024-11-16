class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"
    

# Define the books and their genres
book_data = {
    "World Classics": [
        Book("1984", "George Orwell"),
        Book("Brave New World", "Aldous Huxley"),
        Book("Life on Loan", "Erich Maria Remarque"),
        Book("The Art of Loving", "Erich Fromm"),
        Book("Arc de Triomphe", "Erich Maria Remarque"),
        Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("Lord of the Flies", "William Golding"),
        Book("The Hitchhiker's Guide to the Galaxy: The Restaurant at the End of the Universe", "Douglas Adams"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("A Clockwork Orange", "Anthony Burgess"),
        Book("The Picture of Dorian Gray", "Oscar Wilde"),
        Book("Letters to a Stranger", "André Maurois"),
        Book("The Man Who Mistook His Wife for a Hat and Other Medical Stories", "Oliver Sacks"),
        Book("Animal Farm: Essay", "George Orwell"),
        
    ],
    "Detectives": [
        Book("The Murder of Roger Ackroyd", "Agatha Christie"),
        Book("The Hound of the Baskervilles", "Arthur Conan Doyle"),
        Book("The Girl with the Dragon Tattoo", "Stieg Larsson"),
        Book("Gone Girl", "Gillian Flynn"),
        Book("Big Little Lies", "Liane Moriarty"),
        Book("The Silent Patient", "Alex Michaelides"),
        Book("In the Woods", "Tana French"),
        Book("The Woman in White", "Wilkie Collins"),
        Book("The Cuckoo's Calling", "Robert Galbraith"),
        Book("Sharp Objects", "Gillian Flynn"),
        Book("And Then There Were None", "Agatha Christie"),
        Book("The Secret History", "Donna Tartt"),
        Book("Before I Go to Sleep", "S.J. Watson"),
        Book("The Couple Next Door", "Shari Lapena"),
        Book("The Girl on the Train", "Paula Hawkins")
    ],
    
    "Fantasy": [
        Book("The Hobbit", "J.R.R. Tolkien"),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
        Book("The Name of the Wind", "Patrick Rothfuss"),
        Book("Mistborn: The Final Empire", "Brandon Sanderson"),
        Book("A Game of Thrones", "George R.R. Martin"),
        Book("The Way of Kings", "Brandon Sanderson"),
        Book("The Final Empire", "Brandon Sanderson"),
        Book("The Lies of Locke Lamora", "Scott Lynch"),
        Book("The Blade Itself", "Joe Abercrombie"),
        Book("The Lightbringer", "Brent Weeks"),
        Book("The Priory of the Orange Tree", "Samantha Shannon"),
        Book("The Black Prism", "Brent Weeks"),
        Book("The Witcher: The Last Wish", "Andrzej Sapkowski"),
        Book("The Broken Earth", "N.K. Jemisin"),
        Book("The Stormlight Archive", "Brandon Sanderson")
    ],
    
    "Psychology": [
        Book("Thinking, Fast and Slow", "Daniel Kahneman"),
        Book("Outliers", "Malcolm Gladwell"),
        Book("The Power of Habit", "Charles Duhigg"),
        Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari"),
        Book("The Psychopath Test", "Jon Ronson"),
        Book("Grit: The Power of Passion and Perseverance", "Angela Duckworth"),
        Book("Blink", "Malcolm Gladwell"),
        Book("Quiet: The Power of Introverts in a World That Can't Stop Talking", "Susan Cain"),
        Book("Drive: The Surprising Truth About What Motivates Us", "Daniel H. Pink"),
        Book("Predictably Irrational", "Dan Ariely"),
        Book("The Subtle Art of Not Giving a F*ck", "Mark Manson"),
        Book("The Social Animal", "Elliot Aronson"),
        Book("The Happiness Hypothesis", "Jonathan Haidt"),
        Book("Daring Greatly", "Brene Brown"),
        Book("Influence: The Psychology of Persuasion", "Robert Cialdini")
    ]
}
