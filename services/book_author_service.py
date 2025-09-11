from services.book_service import BookService
from services.author_service import AuthorService
from storage.book_author_dao import BookAuthorDAO
from models.author import Author
from models.book import Book

class BookAuthorService:
    def __init__(self):
        self.book_author_dao = BookAuthorDAO()

    def add_author_to_book(self, book_id, author_id):
        self.book_author_dao.add_author_to_book(book_id, author_id)

    def get_authors_for_book(self, book_id):
        return self.book_author_dao.get_authors_for_book(book_id)

    def get_books_for_author(self, author_id):
        return self.book_author_dao.get_books_for_author(author_id)
    
    def remove_author_from_book(self, book_id, author_id):
        self.book_author_dao.remove_author_from_book(book_id, author_id)
