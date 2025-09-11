import pytest
import sqlite3
import tempfile
import os
from app import app

# test data
test_book = {
    "id": None,
    "title": "The Pragmatic Programmer",
    "published_year": "1999",
    "isbn": "9780201616224",
    "pages": "352",
    "language": "en",
    "authors": []
}
test_author = {
    "id": None,
    "name": "Andrew Hunt",
    "birth_year": "1973",
    "books": []
}

##################################################################
# ---------------  Test config and mock database --------------- #
##################################################################

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['DATABASE'] = db_path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_year INTEGER
        );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        published_year INTEGER,
        isbn TEXT UNIQUE,
        pages INTEGER,
        language TEXT
        );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS book_authors (
        book_id INTEGER,
        author_id INTEGER,
        PRIMARY KEY (book_id, author_id),
        FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
        FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
        );
    """)

    ##########################################################################
    # --------------- Insert test- book, author and relation --------------- #
    ##########################################################################
    
    cursor.execute(
        "INSERT INTO books (title, published_year, isbn, pages, language) VALUES (?, ?, ?, ?, ?)",
        (test_book["title"], test_book["published_year"], test_book["isbn"], test_book["pages"], test_book["language"])
        )
    test_book["id"] = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO authors (name, birth_year) VALUES (?, ?)",
        (test_author["name"], test_author["birth_year"])
    )
    test_author["id"] = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO book_authors (book_id, author_id) VALUES (?, ?)",
        (test_book["id"], test_author["id"])
    )

    conn.commit()
    conn.close()
    
    with app.test_client() as client:
        yield client
        
    os.close(db_fd)
    os.unlink(db_path)
        
        
        
#########################################
# --------------- Tests --------------- #
#########################################

# book

def test_get_book(client):
    print(test_book["id"])
    response = client.get('/books/' + str(test_book["id"]))
    assert response.status_code == 200
    assert bytes(test_book["title"], "utf-8") in response.data
    assert bytes(test_book["published_year"], "utf-8") in response.data
    assert bytes(test_book["isbn"], "utf-8") in response.data
    assert bytes(test_book["pages"], "utf-8") in response.data
    assert bytes(test_book["language"], "utf-8") in response.data
    assert bytes(test_author["name"], "utf-8") in response.data
    
def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert bytes(test_book["title"], "utf-8") in response.data
    assert bytes(test_book["published_year"], "utf-8") in response.data
    assert bytes(test_book["isbn"], "utf-8") in response.data
    assert bytes(test_book["pages"], "utf-8") in response.data
    assert bytes(test_book["language"], "utf-8") in response.data
    assert bytes(test_author["name"], "utf-8") in response.data
    
def test_create_book(client):
    pass

def test_post_edit_book(client):
    pass

def test_get_edit_book(client):
    pass

# def test_post_delete_book(client):
#     response = client.post('/books/' + str(test_book["id"]) + '/delete')
#     assert response.status_code == 200
    
def test_get_delete_book(client):
    pass

# author

def test_get_author(client):
    response = client.get('/authors/' + str(test_author["id"]))
    assert response.status_code == 200
    assert bytes(test_author["name"], "utf-8") in response.data
    assert bytes(test_author["birth_year"], "utf-8") in response.data
    assert bytes(test_book["title"], "utf-8") in response.data
    
def test_get_authors(client):
    response = client.get('/authors')
    assert response.status_code == 200
    assert bytes(test_author["name"], "utf-8") in response.data
    assert bytes(test_author["birth_year"], "utf-8") in response.data
    assert bytes(test_book["title"], "utf-8") in response.data

def test_create_author(client):
    pass

def test_post_edit_author(client):
    pass

def test_get_edit_author(client):
    pass

def test_post_delete_author(client):
    pass

def test_get_delete_author(client):
    pass

# linking & removing

def test_link_author_book(client):
    pass

def test_remove_author_book(client):
    pass

