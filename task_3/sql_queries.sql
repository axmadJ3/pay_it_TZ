-- Найти общую сумму заказов для каждого клиента
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;

-- Найти клиента с максимальной суммой заказов
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 1;

-- Найти количество заказов, сделанных в 2023 году
SELECT COUNT(*) AS order_count
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2023;

-- Найти среднюю сумму заказа для каждого клиента
SELECT customer_id, AVG(amount) AS avg_order_amount
FROM orders
GROUP BY customer_id;