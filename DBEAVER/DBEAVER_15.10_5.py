-- Находим автора, у которого суммарно продано больше всего книг
SELECT
    a.first_name AS "Имя автора",
    a.last_name AS "Фамилия автора",
    total_sales AS "Всего продано книг"
FROM authors a
JOIN (
    SELECT
        b.author_id,
        SUM(s.quantity) AS total_sales
    FROM books b
    JOIN sales s ON s.book_id = b.id
    GROUP BY b.author_id
) AS author_sales ON author_sales.author_id = a.id
ORDER BY total_sales DESC
LIMIT 1;


-- Находим книги, которые продались лучше среднего уровня продаж
SELECT
    b.title AS "Название книги",
    a.first_name AS "Имя автора",
    a.last_name AS "Фамилия автора",
    s.quantity AS "Продано экземпляров"
FROM sales s
JOIN books b ON s.book_id = b.id
JOIN authors a ON b.author_id = a.id
WHERE s.quantity > (
    SELECT AVG(quantity) FROM sales
)
ORDER BY s.quantity DESC;
