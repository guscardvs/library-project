from initial.entities.book import Book
from initial.repositories.base import Repository
from initial.repositories.error_codes import ErrorCodes


class BookRepository(Repository):
    filename = "book.json"
    default_json = {"books": []}

    def _get_books(self) -> list[Book]:
        data = self._read_data()
        return [Book(**item) for item in data["books"]]

    def exists(self, book: Book):
        books = self._get_books()
        return any(item.is_equal(book) for item in books)
    
    def _create_book(self, book: Book) -> bool:
        books = self._get_books()
        books.insert(0, book)
        response = self.default_json.copy()
        response["books"] = [item.serialize() for item in books]
        self._persist_data(response)
        return True

    def create_book(self, book_dict: dict[str, str]) -> ErrorCodes:
        book = Book(**book_dict)
        if self.exists(book):
            return ErrorCodes.already_exists
        if not self._create_book(book):
            return ErrorCodes.unexpected_error
        return ErrorCodes.successful
