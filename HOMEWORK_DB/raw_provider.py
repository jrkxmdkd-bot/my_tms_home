import psycopg
from data_provider import DataProvider
from db_logic.raw_sql_queries import CREATE_TABLE_QUERIES, INSERT_AUTHOR, INSERT_BOOK, INSERT_BOOK_GENRE


class RawSqlProvider(DataProvider):
    connection = None

    @staticmethod
    def connect():
        if not RawSqlProvider.connection or RawSqlProvider.connection.closed:
            print('Create new connection')
            RawSqlProvider.connection = psycopg.connect("dbname=console-app user=postgres password=postgres host=localhost")
            return RawSqlProvider.connection

        print('Use existing connections')
        return RawSqlProvider.connection

    @staticmethod
    def create_tables():
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                for q in CREATE_TABLE_QUERIES:
                    cur.execute(q)


    @staticmethod
    def add_author(name):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_AUTHOR, (name,))
                result = cur.fetchone()
                return cur.fetchone()[0]

    @staticmethod
    def add_book(*args):
        title, publication_year, author_id = args
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_BOOK, (title, publication_year, author_id))
                result = cur.fetchone()
                return cur.fetchone()[0]

    @staticmethod
    def add_book_genre(genre_name):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_BOOK_GENRE, (genre_name,))
                return cur.fetchone()[0]

    @staticmethod
    def get_books_by_genre(genre_name):
        pass

    @staticmethod
    def get_boks_by_author_add_year(author_name, year):
        pass