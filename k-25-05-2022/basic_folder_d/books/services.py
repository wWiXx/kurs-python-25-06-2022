
from abc import abstractmethod, ABC
from typing import List

from books.utils import read_from_csv


class BookProvider(ABC):

    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def get_book(self, id):
        pass


class BookCsvProvider(BookProvider):

    def get_all_books(self):
        books = read_from_csv("books/data/data.csv")
        return books

    def get_book(self, id):
        books = read_from_csv("books/data/data.csv")
        return books[id - 1]


# class BookApiProvider(BookProvider):
#
#     def get_all_books(self) -> List[BookObject]:
#         books = read_from_csv("books/data/data.csv")
#         return books


class ModelsBooksProvider(BookProvider):

    def get_all_books(self):
        pass

    def get_book(self, id):
        pass


class BookService:

    def __init__(self, provider: BookProvider):
        self.provider = provider

    def get_all_books(self):
        return self.provider.get_all_books()

    def get_book(self, book_id):
        return self.provider.get_book(book_id)


provider = BookCsvProvider()
book_service = BookService(provider=provider)
