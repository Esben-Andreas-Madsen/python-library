from app.extensions import db
from app.models.book import Book
from app.models.author import Author

# seed.py
from app.extensions import db
from app.models.book import Book
from app.models.author import Author

from sqlalchemy import text
from app.extensions import db
from app.models.book import Book
from app.models.author import Author

def seed_data():
    """Insert sample books, authors, and many-to-many relations safely."""
    
    # --- Clear existing data ---
    db.session.execute(text("DELETE FROM book_authors"))
    db.session.query(Book).delete()
    db.session.query(Author).delete()
    db.session.commit()

    # --- Create authors ---
    author1 = Author(name="J.K. Rowling", birth_year=1965)
    author2 = Author(name="George Orwell", birth_year=1903)
    author3 = Author(name="Isaac Asimov", birth_year=1920)
    db.session.add_all([author1, author2, author3])
    db.session.commit()  # commit to assign IDs

    # --- Create books ---
    book1 = Book(
        title="Harry Potter and the Philosopher's Stone",
        published_year=1997,
        isbn="9780747532699",
        pages=223,
        language="English"
    )
    book2 = Book(
        title="1984",
        published_year=1949,
        isbn="9780451524935",
        pages=328,
        language="English"
    )
    book3 = Book(
        title="Animal Farm",
        published_year=1945,
        isbn="9780451526342",
        pages=112,
        language="English"
    )
    book4 = Book(
        title="Foundation",
        published_year=1951,
        isbn="9780553293357",
        pages=255,
        language="English"
    )
    book5 = Book(
        title="I, Robot",
        published_year=1950,
        isbn="9780553294385",
        pages=224,
        language="English"
    )
    db.session.add_all([book1, book2, book3, book4, book5])
    db.session.commit()

    book1.authors.extend([author1])
    book2.authors.extend([author2])
    book3.authors.extend([author2])
    book4.authors.extend([author3])
    book5.authors.extend([author3])

    db.session.commit()
    print("Seed data inserted successfully!")


