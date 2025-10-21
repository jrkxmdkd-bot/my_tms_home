# Запросы для создания таблиц
CREATE_AUTHORS_TABLE = """
 CREATE TABLE IF NOT EXISTS authors (
     author_id SERIAL PRIMARY KEY,
     author_name VARCHAR(255) NOT NULL
 );
 """

CREATE_GENRES_TABLE = """
 CREATE TABLE IF NOT EXISTS genres (
     genre_id SERIAL PRIMARY KEY,
     genre_name VARCHAR(255) NOT NULL
 );
 """

CREATE_BOOKS_TABLE = """
 CREATE TABLE IF NOT EXISTS books (
     book_id SERIAL PRIMARY KEY,
     title VARCHAR(255) NOT NULL,
     publication_year INT,
     author_id INT,
     FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
 );
 """

CREATE_BOOK_GENRES_TABLE = """
CREATE TABLE IF NOT EXISTS book_genres (
    book_id INT,
    genre_id INT,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);
"""

CREATE_TABLE_QUERIES = [CREATE_AUTHORS_TABLE, CREATE_GENRES_TABLE, CREATE_BOOKS_TABLE, CREATE_BOOK_GENRES_TABLE]

# Запросы на добавление данных
INSERT_AUTHOR = "INSERT INTO authors (author_name) VALUES (%s) RETURNING author_id;"
INSERT_GENRE = "INSERT INTO genres (genre_name) VALUES (%s) RETURNING genre_id;"
INSERT_BOOK = "INSERT INTO books (title, publication_year, author_id) VALUES (%s, %s, %s) RETURNING book_id;"
INSERT_BOOK_GENRE = "INSERT INTO book_genres (book_id, genre_id) VALUES (%s, %s) RETURNING book_id, genre_id;"

INSET_TABLE_QUERIES = [INSERT_AUTHOR, INSERT_GENRE, INSERT_BOOK, INSERT_BOOK_GENRE]
