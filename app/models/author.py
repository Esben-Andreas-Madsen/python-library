# app/models/author_sql.py
from app.extensions import db
from app.models.book_author import book_authors

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.Integer)

    books = db.relationship(
        "Book",
        secondary=book_authors,
        back_populates="authors"
    )
