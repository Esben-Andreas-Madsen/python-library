import pytest
from app import create_app, init_db
from configs.test_config import TestConfig
from app.extensions import db
from app.models.author import Author
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        init_db(app)
        
        # create test objects
        test_author = Author(name="Andrew Hunt", birth_year=1973)
        test_book = Book(
            title="The Pragmatic Programmer",
            published_year=1999,
            isbn="9780201616224",
            pages=352,
            language="en"
        )

        test_book.authors.append(test_author)

        db.session.add_all([test_author, test_book])
        db.session.commit()
        
        # save reference
        app.test_author = test_author
        app.test_book = test_book
        
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_book_by_id_html(client, app):
    # arrange
    book = app.test_book
    author = app.test_author
    
    # act
    response = client.get(f"/books/{book.id}")
    
    # assert
    assert response.status_code == 200
    assert book.title.encode() in response.data
    assert author.name.encode() in response.data


