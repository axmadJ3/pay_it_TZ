import os
import time
import psycopg2

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}


def connect_db():
    """Ожидаем запуск БД и подключаемся"""
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            return conn
        except psycopg2.OperationalError:
            print("Ожидание запуска БД...")
            time.sleep(2)


def create_table():
    """Создает таблицу products, если она не существует."""
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                price NUMERIC(10, 2) NOT NULL,
                quantity INTEGER NOT NULL
            )
        """
        )
        conn.commit()


def insert_products():
    """Добавляет 10 тестовых продуктов в таблицу."""
    products = [
        ("Apple", 1.2, 15),
        ("Banana", 0.8, 8),
        ("Orange", 1.5, 5),
        ("Grapes", 2.0, 20),
        ("Mango", 2.5, 3),
        ("Peach", 1.8, 12),
        ("Strawberry", 3.0, 7),
        ("Pineapple", 2.8, 4),
        ("Blueberry", 4.0, 6),
        ("Watermelon", 5.0, 1),
    ]

    with connect_db() as conn, conn.cursor() as cursor:
        cursor.executemany(
            "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", products
        )
        conn.commit()


def get_low_stock_products():
    """Возвращает список продуктов с количеством меньше 10."""
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE quantity < 10")
        return cursor.fetchall()


def update_price(product_name, new_price):
    """Обновляет цену продукта по имени."""
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute("UPDATE products SET price = %s WHERE name = %s", (new_price, product_name))
        conn.commit()


if __name__ == "__main__":
    create_table()
    insert_products()

    print("Продукты с малым количеством:")
    print(get_low_stock_products())

    update_price("Apple", 1.5)
    print("Цена обновлена.")
