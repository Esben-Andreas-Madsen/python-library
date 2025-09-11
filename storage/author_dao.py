import sqlite3
from models.author import Author

class AuthorDAO:
    def __init__(self, db_path="./storage/library.db"):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_author(self, author: Author) -> Author:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name, birth_year) VALUES (?, ?)",
            (author.name, author.birth_year)
        )
        author.id = cursor.lastrowid # returns PK
        conn.commit()
        conn.close()
        return author

    def get_author_by_id(self, author_id) -> Author:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, birth_year FROM authors WHERE id=?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Author(id=row[0], name=row[1], birth_year=row[2])
        return None

    def get_all_authors(self) -> list[Author]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, birth_year FROM authors")
        rows = cursor.fetchall()
        conn.close()
        authors = []
        for row in rows:
            author = Author(id=row[0], name=row[1], birth_year=row[2])
            authors.append(author)
        return authors

    def update_author(self, author: Author):
        if author.id is None:
            raise ValueError("Author must have an id to be updated")
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE authors SET name=?, birth_year=? WHERE id=?",
            (author.name, author.birth_year, author.id)
        )
        conn.commit()
        conn.close()

    def delete_author(self, author_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id=?", (author_id,))
        conn.commit()
        conn.close()
    
    def get_author_by_name(self, name) -> Author:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, birth_year FROM authors WHERE name=?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Author(id=row[0], name=row[1], birth_year=row[2])
        return None