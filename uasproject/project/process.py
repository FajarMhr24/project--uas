from data import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def get_books(self):
        return self.books



