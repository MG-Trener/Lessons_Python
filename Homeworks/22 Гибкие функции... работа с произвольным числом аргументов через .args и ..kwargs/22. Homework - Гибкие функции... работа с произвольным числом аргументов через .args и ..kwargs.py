#  Задача 1: «Список гостей»
#  Напишите функцию invite_guests(*names), которая принимает любое
#  количество имен. Функция должна вывести фразу:
#  «Приглашенные гости: [имя1], [имя2], ...»,
#  объединив все имена через запятую.
#
def invite_guests(*names):
    if names:
        return "Приглашенные гости: " + ", ".join(names) # объединяем несколько имен в одну строку
    else:
        return "Гости не указаны"

print(invite_guests("Али", "Мария", "Иван"))
print(invite_guests())
#
#  Задача 2: «Сумматор цен»
#  Создайте функцию total_sum(*prices). Она должна принимать
#  произвольное количество цен товаров и возвращать их сумму.
#  Если аргументов нет, функция должна вернуть 0.

def total_sum(*prices):
    return sum(prices)

print(total_sum(100, 250, 50, 11))
print(total_sum())

#  Задача 3: «Визитка»
#  Напишите функцию make_profile(**info). Она принимает
#  именованные аргументы (например, name="Али", age=20, city="Almaty").
#  Функция должна вывести их в формате: «Ключ: Значение».

def make_profile(**info):
    result = []
    for key, value in info.items():
        result.append(f"{key}: {value}")
    return result

print(make_profile(name="Али", age=20, city="Almaty"))
#
#  Задача 4: «Проверка наличия»
#  Напишите функцию is_included(target, *items).
#  Первый аргумент - это искомый элемент,
#  остальные - список элементов для поиска.
#  Функция должна вернуть True, если target есть среди items,
#  иначе - False.
#
def is_included(target, *items):
    return target in items

print(is_included(8, 1, 2, 3, 4, 5))
#
#  Задача 5: «Счетчик аргументов»
#  Создайте функцию args_count(*args, **kwargs).
#  Она должна возвращать сообщение:
#  «Вы передали [N] позиционных и [M] именованных аргументов».
#
def args_count(*args, **kwargs):
    return f"Вы передали {len(args)} позиционных и {len(kwargs)} именованных аргументов"

print(args_count(1, 4, 4, 2, 3, name="Али", age=20, city = 'Astana'))
#
#  Задача 6: «Калькулятор калорий»
#  Напишите функцию calculate_calories(*foods, **details).
#  foods - это кортеж с названиями продуктов.
#  details - это дополнительные данные, например is_diet=True.
#  Функция должна вывести список продуктов.
#  Если is_diet=True, в конце добавить надпись:
#  «(Диетический рацион)».

def calculate_calories(*foods, **details):
    result = "Продукты: " + ", ".join(foods)
    if details.get("is_diet") == True:
        result += " (Диетический рацион)"
    return result

print(calculate_calories("Яблоко", "Курица", is_diet=True))
#
#  Задача 7: «Минимальное и максимальное»
#  Создайте функцию min_max_search(mode, *numbers).
#  Если mode="min", функция возвращает минимальное число из *numbers.
#  Если mode="max", то максимальное.
#  Если передано что-то другое - вернуть «Ошибка режима».
#
def min_max_search(mode:str, *numbers):
    if not numbers:
        return "Нет чисел"
    if mode == "min":
        return min(numbers)
    elif mode == "max":
        return max(numbers)
    else:
        return "Ошибка режима"

print(min_max_search("min", 10, 3, 8, 1))
print(min_max_search("max", 10, 3, 8, 1))
print(min_max_search("other ", 10, 3, 8, 1))
#
#  Задача 8: «Умный логгер»
#  Напишите функцию log_message(message, **metadata).
#  Она выводит основное сообщение, а затем все дополнительные
#  данные из metadata в скобках.
#  Пример:
#  log_message("Ошибка сервера", code=500, time="12:00")
#  Вывод:
#  Ошибка сервера (code: 500, time: 12:00)
#
def log_message(message, **metadata):
    if metadata:
        meta_str = ", ".join(f"{k}: {v}" for k, v in metadata.items())
        return f"{message} ({meta_str})"
    return message

print(log_message("Ошибка сервера", code=500, time="12:00"))
#
#  Задача 9: «Слияние словарей»
#  Напишите функцию merge_configs(**configs).
#  Она должна принимать несколько словарей через именованные аргументы
#  и возвращать один большой словарь, где все ключи
#  в верхнем регистре (UPPERCASE).

def merge_configs(**configs):
    merged = {}
    for config in configs.values():
        for key, value in config.items():
            merged[key.upper()] = value
    return merged

config1 = {"host": "localhost"}
config2 = {"port": 8080}
print(merge_configs(first=config1, second=config2))
#
#  Задача 10: «Математический бонус»
#  Создайте функцию power_up(power, *numbers).
#  Первый аргумент - степень.
#  Все остальные числа нужно возвести в эту степень
#  и вернуть результат в виде списка.
#  Пример вызова:
#  power_up(2, 1, 2, 3) -> [1, 4, 9]

def power_up(power, *numbers):
    return [num ** power for num in numbers]

print(power_up(2, 1, 2, 3))