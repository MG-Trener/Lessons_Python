# ============================================================
# Задача 1: «Сумматор только чисел»
# Напишите функцию sum_only_numbers(*args), которая принимает любые
# типы данных, но складывает только целые числа (int) и числа с плавающей
# точкой (float).
# Пример вывода:
# sum_only_numbers(10, "hi", 5.5, True) -> 15.5
# ============================================================

def sum_only_numbers(*args):  # принимает любое количество позиционных аргументов
    total = 0  # переменная для хранения суммы
    for item in args:  # перебираем каждый аргумент
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            # проверяем, является ли элемент int или float
            # bool исключаем, потому что True = 1, False = 0
            total += item  # прибавляем число к сумме
    return total  # возвращаем результат

print(sum_only_numbers(10, "hi", 5.5, True))


# ============================================================
# Задача 2: «Поиск самого длинного слова»
# Напишите функцию find_longest_word(*words), которая находит самое
# длинное слово среди переданных.
# Пример вывода:
# find_longest_word("apple", "banana", "cherry") -> "banana"
# ============================================================

def find_longest_word(*words):  # принимает любое количество слов
    longest = ""  # переменная для хранения самого длинного слова
    for word in words:  # перебираем слова
        if len(word) > len(longest):  # сравниваем длину
            longest = word  # если слово длиннее — сохраняем
    return longest  # возвращаем самое длинное слово

print(find_longest_word("apple", "banana", "cherry"))


# ============================================================
# Задача 3: «Фильтр по критериям»
# Напишите функцию filter_by_criteria(**kwargs), которая выводит только те
# ключи, значение которых длиннее 5 символов.
# Пример вывода:
# filter_by_criteria(city="Almaty", name="Jo", job="Developer") -> city, job
# ============================================================

def filter_by_criteria(**kwargs):  # принимает именованные аргументы
    result = []  # список для хранения подходящих ключей
    for key, value in kwargs.items():  # перебираем словарь
        if len(str(value)) > 5:  # проверяем длину значения
            result.append(key)  # добавляем ключ
    return result  # возвращаем список

print(filter_by_criteria(city="Almaty", name="Jo", job="Developer"))


# ============================================================
# Задача 4: «Средний балл по предметам»
# Создайте функцию calculate_scores(student_name, **subjects).
# Она должна выводить имя студента и его средний балл.
# Пример вывода:
# calculate_scores("Alikhan", math=90, eng=80) -> Alikhan: 85.0
# ============================================================

def calculate_scores(student_name, **subjects):
    total = 0  # сумма баллов
    count = 0  # количество предметов
    for score in subjects.values():  # перебираем оценки
        total += score  # складываем
        count += 1  # считаем предметы
    average = total / count if count > 0 else 0  # вычисляем среднее
    return f"{student_name}: {average}"  # возвращаем строку

print(calculate_scores("Alikhan", math=90, eng=80))


# ============================================================
# Задача 5: «Поиск по тегам»
# Напишите функцию has_tag(target_tag, *tags), которая проверяет,
# есть ли искомый тег в списке. Регистр не должен иметь значения.
# Пример вывода:
# has_tag("Python", "python", "Java", "C++") -> True
# ============================================================

def has_tag(target_tag, *tags):
    target_tag = target_tag.lower()  # приводим к нижнему регистру
    for tag in tags:  # перебираем теги
        if tag.lower() == target_tag:  # сравниваем без учета регистра
            return True
    return False

print(has_tag("Python", "python", "Java", "C++"))


# ============================================================
# Задача 6: «Сборщик уникальных элементов»
# Напишите функцию get_unique_elements(*args), которая возвращает список
# только уникальных элементов, переданных в *args.
# Пример вывода:
# get_unique_elements(1, 2, 2, 3, "a", "a") -> [1, 2, 3, 'a']
# ============================================================

def get_unique_elements(*args):
    unique = []  # список уникальных элементов
    for item in args:
        if item not in unique:  # проверяем, нет ли элемента уже в списке
            unique.append(item)
    return unique

print(get_unique_elements(1, 2, 2, 3, "a", "a"))


# ============================================================
# Задача 7: «Генератор ценника»
# Напишите функцию format_price_list(**items). Она должна выводить
# товары, цена которых выше 500.
# Пример вывода:
# format_price_list(milk=450, cheese=1200, bread=200) -> cheese: 1200
# ============================================================

def format_price_list(**items):
    result = {}  # словарь подходящих товаров
    for name, price in items.items():
        if price > 500:  # фильтр по цене
            result[name] = price
    return result

print(format_price_list(milk=450, cheese=1200, bread=200))


# ============================================================
# Задача 8: «Объединитель со словарем»
# Напишите функцию build_dict(*keys, value="Unknown").
# Она принимает список ключей и создает словарь, где у каждого ключа
# будет одно и то же значение по умолчанию.
# Пример вывода:
# build_dict("id", "name", "age", value="None")
# -> {'id': 'None', 'name': 'None', 'age': 'None'}
# ============================================================

def build_dict(*keys, value="Unknown"):
    result = {}  # создаем пустой словарь
    for key in keys:
        result[key] = value  # каждому ключу присваиваем значение
    return result

print(build_dict("id", "name", "age", value="None"))


# ============================================================
# Задача 9: «Множитель списка»
# Напишите функцию multiply_all(factor, *numbers).
# Она должна умножить каждое число из *numbers на factor
# и вернуть результат в виде списка.
# Пример вывода:
# multiply_all(2, 1, 2, 3) -> [2, 4, 6]
# ============================================================

def multiply_all(factor, *numbers):
    result = []  # список для результата
    for number in numbers:
        result.append(number * factor)  # умножаем
    return result

print(multiply_all(2, 1, 2, 3))


# ============================================================
# Задача 10: «Проверка на пустые аргументы»
# Напишите функцию check_data(*args, **kwargs).
# Она должна возвращать True, если переданы хотя бы какие-то данные,
# и False, если функция вызвана пустой.
# Пример вывода:
# check_data() -> False;
# check_data(1) -> True
# ============================================================

def check_data(*args, **kwargs):
    return bool(args or kwargs)
    # if args or kwargs:  # если есть данные
    #     return True
    # return False  # если ничего не передано


print(check_data())
print(check_data(1))