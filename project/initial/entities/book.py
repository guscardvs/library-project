from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Book:
    name: str
    _id: str
    author: str
    year: int
    publisher: str

    def serialize(self):
        return {
            "name": self.name,
            "_id": self._id,
            "author": self.author,
            "year": self.year,
            "publisher": self.publisher,
        }

    @property
    def id(self):
        return self._id

    def is_equal(self, book: "Book"):
        return self.id == book.id
