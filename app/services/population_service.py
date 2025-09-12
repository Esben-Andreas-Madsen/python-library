from app.services.book_service import BookService
from app.services.author_service import AuthorService
from app.services.book_author_service import BookAuthorService

class PopulationService:
    def __init__(self):
        self.book_service = BookService()
        self.author_service = AuthorService()
        self.book_author_service = BookAuthorService()

    def populate_sample_data(self):
        """
            Inserts some dummy data to make the library seem less empty
        """
        samples = [
            {
                "title": "The Pragmatic Programmer",
                "published_year": "1999",
                "isbn": "9780201616224",
                "pages": 352,
                "language": "en",
                "authors": [{"name":" Andrew Hunt", "birth_year": 1973}, {"name":" David Thomas"}]
            },
            {
                "title": "Clean Code",
                "published_year": "2008",
                "isbn": "9780132350884",
                "pages": 464,
                "language": "en",
                "authors": [{"name": "Robert C. Martin"}]
            },
            {
                "title": "Python Crash Course",
                "published_year": "2015",
                "isbn": "9781593276034",
                "pages": 560,
                "language": "en",
                "authors": [{"name": "Eric Matthes", "birth_year": 1973}, {"name": "Jeff"}]
            }
        ]

        for sample in samples:
            book = self.book_service.create_book(
                sample["title"],
                sample["published_year"],
                sample["isbn"],
                sample["pages"],
                sample["language"]
            )
            for author in sample["authors"]:
                author = self.author_service.create_author(author.get("name"), author.get("birth_year", None))
                self.book_author_service.add_author_to_book(book.id, author.id)
                