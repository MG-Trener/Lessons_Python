# Задача 5: «Масштабирование списка» (Модуль list_tool.py)
# Что сделать: Модуль с функцией multiply_list(numbers, factor),
# оторая умножает каждое число в списке на factor. Пример вывода: [1, 2, 3] * 10 -> [10, 20, 30]


def multiply_list(numbers, factor):
    result = []
    for number in numbers:
        result.append(number*factor)
    return result