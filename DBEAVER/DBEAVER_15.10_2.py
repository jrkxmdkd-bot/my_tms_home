-- Получаем список всех книг и их авторов
SELECT
    books.title AS "Название книги",
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора"
FROM books
INNER JOIN authors ON books.author_id = authors.id;


-- Получаем список всех авторов и их книг
SELECT
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора",
    books.title AS "Название книги"
FROM authors
LEFT JOIN books ON books.author_id = authors.id;


-- Получаем список всех книг и их авторов
SELECT
    books.title AS "Название книги",
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора"
FROM authors
RIGHT JOIN books ON books.author_id = authors.id;
