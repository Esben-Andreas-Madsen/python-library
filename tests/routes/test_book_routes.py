def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_get_book_by_id(client, book, author):
    response = client.get(f"/books/{book.id}")
    assert response.status_code == 200
    assert book.title.encode() in response.data
    assert author.name.encode() in response.data

def test_get_books(client, book, author):
    response = client.get(f"/books")
    assert response.status_code == 200
    assert book.title.encode() in response.data
    assert author.name.encode() in response.data

def test_edit_book(client, book):
    response = client.get(f"/books/{book.id}/edit")
    assert response.status_code == 200
    assert book.title.encode() in response.data
    
def test_delete_book(client, book, author):
    response = client.post(f"/books/{book.id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert book.title.encode() not in response.data
    assert author.name.encode() not in response.data
    
def test_create_book(client):
    # arrange - new book data
    new_book_data = {
        "title": "Clean Code",
        "published_year": 2008,
        "isbn": "9780132350884",
        "pages": 464,
        "language": "en",
    }
    
    # act - send POST request
    response = client.post(
        "/books/create",
        data=new_book_data,
        follow_redirects=True
    )
    
    # assert - check response
    assert response.status_code == 200
    assert b"Clean Code" in response.data
    assert b"2008" in response.data
    assert b"9780132350884" in response.data
    assert b"464" in response.data
    assert b"en" in response.data