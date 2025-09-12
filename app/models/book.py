# app/models/book_sql.py
from app.extensions import db
from app.models.book_author import book_authors

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    published_year = db.Column(db.Integer)
    isbn = db.Column(db.String, unique=True)
    pages = db.Column(db.Integer)
    language = db.Column(db.String)

    authors = db.relationship(
        "Author",
        secondary=book_authors,
        back_populates="books"
    )
