class Book:
    def __init__(self, id=None, title=None, published_year=None, isbn=None, pages=None, language=None):
        self._id = id
        self._title = title
        self._published_year = published_year
        self._isbn = isbn
        self._pages = pages
        self._language = language
        self._authors = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def published_year(self):
        return self._published_year

    @published_year.setter
    def published_year(self, value):
        self._published_year = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    @property
    def authors(self):
        return self._authors

    def add_author(self, author):
        if author not in self._authors:
            self._authors.append(author)
            author.add_book(self)
    
    @authors.setter
    def authors(self, value):
        self._authors = value

    def __repr__(self):
        return f"Book(id={self._id}, title='{self._title}', published_year={self._published_year})"