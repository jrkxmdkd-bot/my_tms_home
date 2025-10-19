-- Получаем список всех книг, их авторов и количество продаж
SELECT
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора",
    books.title AS "Название книги",
    sales.quantity AS "Количество продаж"
FROM authors
INNER JOIN books ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id;


-- Получаем список всех авторов, их книг и продаж
SELECT
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора",
    books.title AS "Название книги",
    sales.quantity AS "Количество продаж"
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id;