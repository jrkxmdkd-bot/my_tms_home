CREATE TABLE Employees (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Position VARCHAR(50),
    Department VARCHAR(50),
    Salary NUMERIC(10, 2)
);

INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('Иван Петров', 'Engineer', 'Production', 4500.00),
('Мария Кузнецова', 'Manager', 'Sales', 6500.00),
('Алексей Смирнов', 'Analyst', 'Finance', 5200.00),
('Ольга Иванова', 'Engineer', 'Production', 4700.00),
('Дмитрий Орлов', 'Manager', 'IT', 7000.00);

UPDATE Employees
SET Position = 'Senior Engineer', Salary = 5500.00
WHERE Name = 'Ольга Иванова';

ALTER TABLE Employees ADD COLUMN HireDate DATE;

UPDATE Employees
SET HireDate = DATE '2021-05-10'
WHERE Name = 'Иван Петров';

UPDATE Employees
SET HireDate = DATE '2020-08-15'
WHERE Name = 'Мария Кузнецова';

UPDATE Employees
SET HireDate = DATE '2022-02-01'
WHERE Name = 'Алексей Смирнов';

UPDATE Employees
SET HireDate = DATE '2021-11-20'
WHERE Name = 'Ольга Иванова';

UPDATE Employees
SET HireDate = DATE '2019-07-05'
WHERE Name = 'Дмитрий Орлов';

SELECT * FROM Employees
WHERE Position = 'Manager';

SELECT * FROM Employees
WHERE Salary > 5000;

SELECT * FROM Employees
WHERE Department = 'Sales';

SELECT AVG(Salary) AS AverageSalary
FROM Employees;

DROP TABLE Employees;
