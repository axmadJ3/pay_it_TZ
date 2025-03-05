-- Основные SQL-команды в psql

-- Проверить список таблиц:  
\dt

-- Посмотреть структуру таблицы products:  
\d products

-- Вывести все продукты 
SELECT * FROM products;

-- Найти товары с количеством < 10  
SELECT * FROM products WHERE quantity < 10;

-- Обновить цену продукта (например, Apple → 2.0) 
UPDATE products SET price = 2.0 WHERE name = 'Apple';

-- Добавить новый продукт 
INSERT INTO products (name, price, quantity) VALUES ('Cherry', 3.5, 9);

-- Удалить продукт  
DELETE FROM products WHERE name = 'Cherry';

-- Выйти из psql  
\q