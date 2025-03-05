# Входные данные
employees = [
    {"name": "Иван", "position": "разработчик", "salary": 55000},
    {"name": "Анна", "position": "аналитик", "salary": 48000},
    {"name": "Петр", "position": "тестировщик", "salary": 52000},
]


def list_of_names(employees):
    """Список имен сотрудников с зарплатой больше 50 000"""
    return [employee["name"] for employee in employees if employee["salary"] > 50000]


def avg_salary(employees):
    """Средняя зарплата сотрудников"""
    if not employees:
        return 0  # Защита от деления на 0
    return sum(map(lambda emp: emp["salary"], employees)) / len(employees)


def sort_by_salary(employees):
    """Сортировка сотрудников по зарплате"""
    return sorted(employees, key=lambda emp: emp["salary"], reverse=True)


def main():
    print("Список имен сотрудников с зарплатой больше 50 000:", list_of_names(employees))
    print("Средняя зарплата сотрудников:", avg_salary(employees))
    print("Сортировка сотрудников по зарплате:", sort_by_salary(employees))


if __name__ == "__main__":
    main()
