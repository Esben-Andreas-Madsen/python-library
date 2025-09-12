# app/models/book_author_sql.py
from app.extensions import db

book_authors = db.Table(
    'book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)
