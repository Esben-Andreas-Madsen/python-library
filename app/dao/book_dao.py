from app.models.book import Book
from app.extensions import db

class BookDAO:
    def create_book(self, book: Book) -> Book:
        db_book = Book(
            title=book.title,
            published_year=book.published_year,
            isbn=book.isbn,
            pages=book.pages,
            language=book.language
        )
        db.session.add(db_book)
        db.session.commit()
        book.id = db_book.id
        return book

    def get_book_by_id(self, book_id) -> Book | None:
        book = db.session.get(Book, book_id)
        if book:
            return Book(
                id=book.id,
                title=book.title,
                published_year=book.published_year,
                isbn=book.isbn,
                pages=book.pages,
                language=book.language
            )
        return None

    def get_book_by_isbn(self, isbn) -> Book | None:
        db_book = Book.query.filter_by(isbn=isbn).first()
        if db_book:
            return Book(
                id=db_book.id,
                title=db_book.title,
                published_year=db_book.published_year,
                isbn=db_book.isbn,
                pages=db_book.pages,
                language=db_book.language
            )
        return None

    def get_all_books(self) -> list[Book]:
        db_books = Book.query.all()
        return [
            Book(
                id=b.id,
                title=b.title,
                published_year=b.published_year,
                isbn=b.isbn,
                pages=b.pages,
                language=b.language
            ) for b in db_books
        ]

    def update_book(self, book: Book):
        if book.id is None:
            raise ValueError("Book must have an id to be updated")
        db_book = Book.query.get(book.id)
        if not db_book:
            raise ValueError("Book does not exist in the database")
        db_book.title = book.title
        db_book.published_year = book.published_year
        db_book.isbn = book.isbn
        db_book.pages = book.pages
        db_book.language = book.language
        db.session.commit()

    def delete_book(self, book_id):
        db_book = Book.query.get(book_id)
        if db_book:
            db.session.delete(db_book)
            db.session.commit()
