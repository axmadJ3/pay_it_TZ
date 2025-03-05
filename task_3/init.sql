-- Создание таблицы клиентов
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    amount NUMERIC(10,2) NOT NULL
);

INSERT INTO orders (customer_id, order_date, amount) VALUES
(1, '2023-01-15', 100.50),
(2, '2023-05-20', 250.75),
(1, '2023-07-10', 300.00),
(3, '2023-08-05', 500.99),
(2, '2023-12-31', 150.00);
