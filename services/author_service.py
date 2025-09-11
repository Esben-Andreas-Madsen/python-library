from models.author import Author
from storage.author_dao import AuthorDAO

class AuthorService:
    def __init__(self):
        self.author_dao = AuthorDAO()

    def create_author(self, name, birth_year=None):
        # TODO: implement better error-handling / inform the user
        existing = self.author_dao.get_author_by_name(name)
        if existing:
            return existing
        author = Author(name=name, birth_year=birth_year)
        return self.author_dao.create_author(author)

    def get_author(self, author_id):
        return self.author_dao.get_author_by_id(author_id)

    def get_all_authors(self):
        return self.author_dao.get_all_authors()

    def update_author(self, author: Author):
        self.author_dao.update_author(author)
        return author

    def delete_author(self, author_id):
        self.author_dao.delete_author(author_id)
        
    def get_author_by_id(self, author_id):
        return self.author_dao.get_author_by_id(author_id)
    
