import sqlite3

# Подключение к базе данных (файл создается, если его нет)
connection = sqlite3.connect('task_1.db')
cursor = connection.cursor()

# 1. Создание таблицы employees
cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary INTEGER NOT NULL
)
'''
)

# 2. Добавление 5 тестовых записей
employees_data = [
    ("Иван", "Разработчик", 55000),
    ("Анна", "Аналитик", 48000),
    ("Петр", "Тестировщик", 52000),
    ("Ольга", "Менеджер", 60000),
    ("Сергей", "Дизайнер", 47000),
]

cursor.executemany(
    "INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", employees_data
)
connection.commit()

# 3. Вывод сотрудников с зарплатой больше 50 000
print("Сотрудники с зарплатой больше 50 000:")
cursor.execute("SELECT * FROM employees WHERE salary > 50000")
for row in cursor.fetchall():
    print(row)

# 4. Обновление зарплаты Ивану до 60 000
cursor.execute("UPDATE employees SET salary = 60000 WHERE name = 'Иван'")
connection.commit()

# 5. Удаление сотрудника Анны
cursor.execute("DELETE FROM employees WHERE name = 'Анна'")
connection.commit()

# Закрытие соединения
connection.close()
print("Операции успешно выполнены.")
