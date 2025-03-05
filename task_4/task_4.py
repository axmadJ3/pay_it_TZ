from csv import DictReader
import sqlite3
from pathlib import Path

DB_PATH = Path("task_4/task_4.db")
CSV_PATH = Path("task_4/datas.csv")


def create_table():
    """Создает таблицу employees, если она не существует."""
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
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
        connection.commit()


def read_csv(file_path):
    """Читает CSV-файл и возвращает список кортежей (name, position, salary)."""
    employees_list = []
    try:
        with file_path.open("r", encoding="utf-8") as file:
            csv_reader = DictReader(file)

            for row in csv_reader:
                try:
                    salary = int(row["salary"])  # Преобразуем зарплату в число
                    employees_list.append((row["name"], row["position"], salary))
                except ValueError:
                    print(
                        f"Ошибка: Некорректное значение зарплаты '{row['salary']}' для {row['name']}. Пропущено."
                    )

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return []

    return employees_list


def insert_data(data):
    """Добавляет данные в таблицу employees."""
    if not data:
        print("Нет данных для вставки.")
        return

    try:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.executemany(
                "INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", data
            )
            connection.commit()
        print(f"Успешно добавлено {len(data)} записей в базу данных.")
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")


def display_table(result):
    """Форматирует и выводит данные в виде таблицы."""
    if not result:
        print("Нет данных.")
        return

    print(f"\n{'ID':<5} {'Имя':<20} {'Должность':<15} {'Зарплата':<10}")
    print("-" * 50)
    for row in result:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<10}")
    print("-" * 50)


def data_manipulating():
    """Меню управления данными."""
    while True:
        print("\nВыберите действие:")
        print("1. Вывести всех сотрудников")
        print("2. Вывести сотрудников по должности")
        print("3. Изменить зарплату сотрудника")
        print("0. Выход")

        try:
            value = int(input("\nВведите номер действия: "))
        except ValueError:
            print("Ошибка: Введите число.")
            continue

        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()

            if value == 1:
                cursor.execute("SELECT * FROM employees")
                result = cursor.fetchall()
                display_table(result)

            elif value == 2:
                position = input("Введите должность: ").strip()
                cursor.execute("SELECT * FROM employees WHERE position = ?", (position,))
                result = cursor.fetchall()
                display_table(result)

            elif value == 3:
                try:
                    employee_id = int(input("Введите ID сотрудника: "))
                    new_salary = int(input("Введите новую зарплату: "))

                    cursor.execute("SELECT id FROM employees WHERE id = ?", (employee_id,))
                    if not cursor.fetchone():
                        print("Ошибка: Сотрудник с таким ID не найден.")
                        continue

                    cursor.execute(
                        "UPDATE employees SET salary = ? WHERE id = ?",
                        (new_salary, employee_id),
                    )
                    connection.commit()
                    print(f"Зарплата сотрудника с ID {employee_id} успешно обновлена.")

                except ValueError:
                    print("Ошибка: ID и зарплата должны быть числами.")

            elif value == 0:
                print("Выход из программы.")
                break

            else:
                print("Ошибка: Введите корректное число от 0 до 3.")


if __name__ == "__main__":
    create_table()
    employees = read_csv(CSV_PATH)
    insert_data(employees)
    data_manipulating()
