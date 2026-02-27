# Задача 1: Сумма цифр числа
# Напишите рекурсивную функцию sum_of_digits(n),
# которая принимает положительное число n
# и возвращает сумму его цифр.
# Пример: sum_of_digits(1234) → 10

def sum_of_digits(n):
    if n < 10:                  # базовый случай: если число однозначное
        return n                # возвращаем само число
    return n % 10 + sum_of_digits(n // 10)  # последняя цифра + рекурсия без неё

print("1.", sum_of_digits(1234))


# Задача 2: Проверка на палиндром (строка)
# Напишите рекурсивную функцию is_palindrome(s),
# которая проверяет, является ли строка палиндромом.
# Пример: is_palindrome("racecar") → True

def is_palindrome(s):
    if len(s) <= 1:             # базовый случай: строка из 0 или 1 символа
        return True
    if s[0] != s[-1]:           # если первый и последний символ не равны
        return False
    return is_palindrome(s[1:-1])  # проверяем строку без крайних символов

print("2.", is_palindrome("racecar"))
print("2.", is_palindrome("hello"))


# Задача 3: Поиск максимального числа в списке
# Напишите рекурсивную функцию find_max(lst),
# которая возвращает максимальное число.
# Пример: find_max([1, 5, 9, 3, 7]) → 9

def find_max(lst):
    if len(lst) == 1:           # базовый случай: если один элемент
        return lst[0]
    max_rest = find_max(lst[1:])  # максимум оставшейся части списка
    return lst[0] if lst[0] > max_rest else max_rest

print("3.", find_max([1, 5, 9, 3, 7]))


# Задача 4: Числа Фибоначчи
# Реализуйте рекурсивную функцию fibonacci(n),
# которая возвращает n-е число Фибоначчи.
# Пример: fibonacci(6) → 8

def fibonacci(n):
    if n <= 1:                  # базовый случай: 0 или 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("4.", fibonacci(6))


# Задача 5: Разворот списка (изменяемый объект)
# Напишите рекурсивную функцию reverse_list(lst, index=0),
# которая изменяет список, переворачивая его.
# Пример: [1,2,3] → [3,2,1]

def reverse_list(lst, index=0):
    if index >= len(lst) // 2:  # базовый случай: дошли до середины
        return
    lst[index], lst[-index - 1] = lst[-index - 1], lst[index]
    reverse_list(lst, index + 1)

numbers = [1, 2, 3, 4, 5]
reverse_list(numbers)
print("5.", numbers)


# Задача 6: Разворот строки (неизменяемый объект)
# Напишите рекурсивную функцию reverse_string(s),
# которая возвращает перевёрнутую строку.
# Пример: reverse_string("hello") → "olleh"

def reverse_string(s):
    if len(s) == 0:             # базовый случай: пустая строка
        return s
    return s[-1] + reverse_string(s[:-1])

print("6.", reverse_string("hello"))


# Задача 7: Подсчёт элементов в списке
# Реализуйте рекурсивную функцию count_elements(lst),
# которая возвращает количество элементов.
# Пример: count_elements([1,2,3]) → 3

def count_elements(lst):
    if not lst:                 # базовый случай: пустой список
        return 0
    return 1 + count_elements(lst[1:])

print("7.", count_elements([1, 2, 3, 4, 5]))


# Задача 8: Умножение без *
# Напишите рекурсивную функцию multiply(a, b),
# которая умножает два числа через сложение.
# Пример: multiply(5, 3) → 15

def multiply(a, b):
    if b == 0:                  # базовый случай: умножение на 0
        return 0
    if b < 0:                   # если b отрицательное
        return -multiply(a, -b)
    return a + multiply(a, b - 1)

print("8.", multiply(5, 3))


# Задача 9: Замена символов в строке
# Напишите рекурсивную функцию replace_char(s, old, new),
# которая заменяет все символы old на new.
# Пример: replace_char("banana","a","o") → "bonono"

def replace_char(s, old, new):
    if not s:                   # базовый случай: пустая строка
        return ""
    first = new if s[0] == old else s[0]
    return first + replace_char(s[1:], old, new)

print("9.", replace_char("banana", "a", "o"))


# Задача 10: Генерация списка от 1 до n
# Реализуйте рекурсивную функцию generate_list(n),
# которая создаёт список от 1 до n.
# Пример: generate_list(5) → [1,2,3,4,5]

def generate_list(n):
    if n == 0:                  # базовый случай
        return []
    return generate_list(n - 1) + [n]

print("10.", generate_list(5))