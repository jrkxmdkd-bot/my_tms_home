from dataclasses import dataclass, field
from typing import Optional, List


class InvalidBookError(Exception):
    pass


class InvalidValueError(InvalidBookError):
    pass


@dataclass(order=True)
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: Optional[int] = field(default=None, compare=False)

    def __post_init__(self):
        if self.pages <= 0:
            raise InvalidValueError("Количество страниц должно быть положительным числом.")
        if self.year <= 0:
            raise InvalidValueError("Год издания должен быть положительным числом.")
        if not self.author or not isinstance(self.author, str):
            raise InvalidValueError("Автор должен быть строкой.")
        if self.price <= 0:
            raise InvalidValueError("Цена должна быть положительным числом.")

    def __str__(self):
        return f"[{self.book_id}] {self.author} — {self.year}, {self.pages} стр., {self.price} руб."


class Library:
    def __init__(self):
        self._books: List[Book] = []
        self._next_id = 1

    def add_book(self, book: Book):
        book.book_id = self._next_id
        self._books.append(book)
        self._next_id += 1

    def get_book_info(self, book_id: int) -> Optional[str]:
        for book in self._books:
            if book.book_id == book_id:
                return str(book)
        return "Книга с таким ID не найдена."

    def find_by_author(self, authors):
        if isinstance(authors, str):
            authors = [authors]
        return [book for book in self._books if book.author in authors]

    def __str__(self):
        return "\n".join(str(book) for book in self._books) or "Библиотека пуста."
