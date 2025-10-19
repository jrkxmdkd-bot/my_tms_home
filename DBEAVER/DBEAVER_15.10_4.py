-- Считаем общее количество проданных книг каждого автора
SELECT
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора",
    SUM(sales.quantity) AS "Всего продано книг"
FROM authors
INNER JOIN books ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name
ORDER BY "Всего продано книг" DESC;


-- Считаем общее количество проданных книг каждого автора, включая тех, у кого продаж нет
SELECT
    authors.first_name AS "Имя автора",
    authors.last_name AS "Фамилия автора",
    COALESCE(SUM(sales.quantity), 0) AS "Всего продано книг"
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name
ORDER BY "Всего продано книг" DESC;
