def algo_func(nums):
    """
    Данная функция принимает на вход список чисел и возвращает:
    1. Количество уникальных чисел.
    2. Второе по величине число в списке.
    3. Список чисел, которые делятся на 3 без остатка.
    """
    unique_nums = len(set(nums))
    sorted_unique_nums = sorted(set(nums))

    if len(sorted_unique_nums) > 1:  # Проверяем, есть ли хотя бы два уникальных числа
        second_max_num = sorted_unique_nums[-2]

    three_decimal_nums = [num for num in nums if num % 3 == 0]

    return (
        f"Количество уникальных чисел: {unique_nums}\n"
        f"Второе по величине число: {second_max_num}\n"
        f"Числа, делящиеся на 3: {three_decimal_nums}"
    )


if __name__ == '__main__':
    nums = [10, 20, 30, 40, 50, 30, 20]
    print(algo_func(nums))
