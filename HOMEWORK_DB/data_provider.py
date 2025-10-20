from abc import ABC, abstractmethod


class DataProvider(ABC):
    @staticmethod
    @abstractmethod
    def connect(cls):
        pass

    @staticmethod
    @abstractmethod
    def create_tables():
        pass

    @staticmethod
    @abstractmethod
    def add_author(name):
        pass

    @staticmethod
    @abstractmethod
    def add_book(*args):
        pass

    @staticmethod
    @abstractmethod
    def add_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def add_book_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def get_books_by_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def get_boks_by_author_add_year(author_name, year):
        pass
