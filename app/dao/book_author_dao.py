# app/dao/book_author_dao.py
from app.models.book import Book
from app.models.author import Author
from app.models.author import Author
from app.extensions import db

class BookAuthorDAO:
    def add_author_to_book(self, book_id: int, author_id: int):
        book = Book.query.get(book_id)
        author = Author.query.get(author_id)
        if book and author and author not in book.authors:
            book.authors.append(author)
            db.session.commit()

    def remove_author_from_book(self, book_id: int, author_id: int):
        book = Book.query.get(book_id)
        author = Author.query.get(author_id)
        if book and author and author in book.authors:
            book.authors.remove(author)
            db.session.commit()

    def get_authors_for_book(self, book_id: int) -> list[Author]:
        book = Book.query.get(book_id)
        if book:
            return [Author(id=a.id, name=a.name, birth_year=a.birth_year) for a in book.authors]
        return []

    def get_books_for_author(self, author_id: int) -> list[Book]:
        author = Author.query.get(author_id)
        if author:
            return [
                Book(
                    id=b.id,
                    title=b.title,
                    published_year=b.published_year,
                    isbn=b.isbn,
                    pages=b.pages,
                    language=b.language
                )
                for b in author.books
            ]
        return []
