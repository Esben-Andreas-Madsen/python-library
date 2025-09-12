from app.models.book import Book
from app.storage.book_dao import BookDAO

class BookService:
    def __init__(self):
        self.book_dao = BookDAO()

    def create_book(self, title, published_year=None, isbn=None, pages=None, language=None) -> Book:
        # TODO: implement better logic and error handling / inform the user
        if isbn:
            existing = self.book_dao.get_book_by_isbn(isbn)
            if existing:
                return existing
        book = Book(
            title=title,
            published_year=published_year,
            isbn=isbn,
            pages=pages,
            language=language
        )
        return self.book_dao.create_book(book)

    def get_book(self, book_id):
        return self.book_dao.get_book_by_id(book_id)

    def get_all_books(self):
        return self.book_dao.get_all_books()

    def update_book(self, book: Book):
        self.book_dao.update_book(book)
        return book

    def delete_book(self, book_id):
        self.book_dao.delete_book(book_id)
        
    def get_book_by_id(self, book_id):
        return self.book_dao.get_book_by_id(book_id)
