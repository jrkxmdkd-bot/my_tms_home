
-- Создаём таблицу с авторами книг
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- Создаём таблицу с книгами
-- Каждая книга связана с автором через author_id
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Создаём таблицу с продажами книг
-- Здесь храним, сколько экземпляров каждой книги было продано
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Добавляем авторов в таблицу authors
INSERT INTO authors (first_name, last_name) VALUES
('Иван', 'Петров'),
('Мария', 'Кузнецова'),
('Алексей', 'Сидоров');

-- Добавляем книги и указываем, кто их написал
INSERT INTO books (title, author_id, publication_year) VALUES
('Путь Поттера', 1, 2019),
('Магия данных', 2, 2021),
('Гарри Поттер', 3, 2020),
('Гарри неПоттер', 2, 2022);

-- Добавляем данные о продажах книг
INSERT INTO sales (book_id, quantity) VALUES
(1, 120),
(2, 85),
(3, 45),
(4, 60);
