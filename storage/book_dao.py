import sqlite3
from models.book import Book

class BookDAO:
    def __init__(self, db_path="./storage/library.db"):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_book(self, book: Book) -> Book:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, published_year, isbn, pages, language) VALUES (?, ?, ?, ?, ?)",
            (book.title, book.published_year, book.isbn, book.pages, book.language)
        )
        book.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return book

    def get_book_by_id(self, book_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, published_year, isbn, pages, language FROM books WHERE id=?",
            (book_id,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Book(
                id=row[0],
                title=row[1],
                published_year=row[2],
                isbn=row[3],
                pages=row[4],
                language=row[5]
            )
        return None

    def get_all_books(self) -> list[Book]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, published_year, isbn, pages, language FROM books")
        rows = cursor.fetchall()
        conn.close()
        books = []
        for row in rows:
            book = Book(
                id=row[0],
                title=row[1],
                published_year=row[2],
                isbn=row[3],
                pages=row[4],
                language=row[5]
            )
            books.append(book)
        return books


    def update_book(self, book: Book):
        if book.id is None:
            raise ValueError("Book must have an id to be updated")
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE books SET title=?, published_year=?, isbn=?, pages=?, language=? WHERE id=?",
            (book.title, book.published_year, book.isbn, book.pages, book.language, book.id)
        )
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()
        conn.close()
        
    def get_book_by_isbn(self, isbn) -> Book | None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, published_year, isbn, pages, language FROM books WHERE isbn=?",
            (isbn,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Book(
                id=row[0],
                title=row[1],
                published_year=row[2],
                isbn=row[3],
                pages=row[4],
                language=row[5]
            )
        return None
