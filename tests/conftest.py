import pytest
from app import create_app, init_db
from configs.test_config import TestConfig
from app.extensions import db
from app.models.author import Author
from app.models.book import Book

@pytest.fixture(scope="function")
def app():
    app = create_app(TestConfig)

    with app.app_context():
        init_db(app)
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def author(app):
    author = Author(name="Andrew Hunt", birth_year=1973)
    db.session.add(author)
    db.session.commit()
    return author

@pytest.fixture
def book(app, author):
    book = Book(
        title="The Pragmatic Programmer",
        published_year=1999,
        isbn="9780201616224",
        pages=352,
        language="en"
    )

    book.authors.append(author)

    db.session.add(book)
    db.session.commit()
    return book
