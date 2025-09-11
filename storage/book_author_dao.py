import sqlite3
from models.author import Author
from models.book import Book

class BookAuthorDAO:
    def __init__(self, db_path="./storage/library.db"):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def add_author_to_book(self, book_id, author_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            # inserts if row doesn't exist
            "INSERT OR IGNORE INTO book_authors (book_id, author_id) VALUES (?, ?)",
            (book_id, author_id)
        )
        conn.commit()
        conn.close()
        
    def remove_author_from_book(self, book_id, author_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM book_authors WHERE book_id = ? AND author_id = ?",
            (book_id, author_id)
        )
        conn.commit()
        conn.close()
        
    def get_authors_for_book(self, book_id) -> list[Author]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.id, a.name, a.birth_year
            FROM authors a
            JOIN book_authors ba ON a.id = ba.author_id
            WHERE ba.book_id = ?
        """, (book_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(id=row[0], name=row[1], birth_year=row[2]) for row in rows]
    
    def get_books_for_author(self, author_id) -> list[Book]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.id, b.title, b.published_year, b.isbn, b.pages, b.language
            FROM books b
            JOIN book_authors ba ON b.id = ba.book_id
            WHERE ba.author_id = ?
        """, (author_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Book(id=row[0], title=row[1], published_year=row[2], isbn=row[3], language=row[4]) for row in rows]
    
    