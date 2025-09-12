from app.models.author import Author
from app.models.author import Author
from app.extensions import db

class AuthorDAO:
    def create_author(self, author: Author) -> Author:
        db_author = Author(name=author.name, birth_year=author.birth_year)
        db.session.add(db_author)
        db.session.commit()
        author.id = db_author.id
        return author

    def get_author_by_id(self, author_id) -> Author:
        db_author = Author.query.get(author_id)
        if db_author:
            return Author(id=db_author.id, name=db_author.name, birth_year=db_author.birth_year)
        return None

    def get_author_by_name(self, name) -> Author:
        db_author = Author.query.filter_by(name=name).first()
        if db_author:
            return Author(id=db_author.id, name=db_author.name, birth_year=db_author.birth_year)
        return None

    def get_all_authors(self) -> list[Author]:
        db_authors = Author.query.all()
        return [Author(id=a.id, name=a.name, birth_year=a.birth_year) for a in db_authors]

    def update_author(self, author: Author):
        db_author = Author.query.get(author.id)
        if not db_author:
            raise ValueError("Author must exist to be updated")
        db_author.name = author.name
        db_author.birth_year = author.birth_year
        db.session.commit()

    def delete_author(self, author_id):
        db_author = Author.query.get(author_id)
        if db_author:
            db.session.delete(db_author)
            db.session.commit()
