class Author:
    def __init__(self, id=None, name=None, birth_year=None):
        self._id = id
        self._name = name
        self._birth_year = birth_year
        self._books = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        self._birth_year = value

    @property
    def books(self):
        return self._books

    def add_book(self, book):
        if book not in self._books:
            self._books.append(book)
            book.add_author(self)
    
    @books.setter
    def books(self, value):
        self._books = value

    def __repr__(self):
        return f"Author(id={self._id}, name='{self._name}', birth_year={self._birth_year})"