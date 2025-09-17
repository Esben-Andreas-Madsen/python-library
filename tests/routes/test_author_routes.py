def test_get_author_by_id(client, book, author):
    response = client.get(f"/authors/{author.id}")
    assert response.status_code == 200
    assert book.title.encode() in response.data
    assert author.name.encode() in response.data

def test_get_authors(client, book, author):
    response = client.get(f"/authors")
    assert response.status_code == 200
    assert book.title.encode() in response.data
    assert author.name.encode() in response.data

def test_edit_author(client, author):
    response = client.get(f"/authors/{author.id}/edit")
    assert response.status_code == 200
    assert author.name.encode() in response.data
    
def test_delete_author(client, book, author):
    response = client.post(f"/authors/{book.id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert book.title.encode() not in response.data
    assert author.name.encode() not in response.data
    
def test_create_author(client):
    new_author_data = {
        "name": "William Shakespeare",
        "birth_year": 1564,
    }
    
    response = client.post(
        "/authors/create",
        data=new_author_data,
        follow_redirects=True
    )
    
    assert response.status_code == 200
    assert b'William Shakespeare' in response.data
    assert b'1564' in response.data