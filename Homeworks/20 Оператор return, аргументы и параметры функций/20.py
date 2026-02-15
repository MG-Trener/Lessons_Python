# Задача 1: «Расчет сдачи»
# Напишите функцию get_change(total_cost, payment).
# Она принимает стоимость товара и сумму, которую дал покупатель. Функция должна
# возвращать размер сдачи. Если денег недостаточно, пусть возвращает отрицательное число.

# def get_change(total_cost, payment):
#     return total_cost - payment
# print(get_change(1000, 600))
# print(get_change(600, 5100))

# Задача 2: «Квадрат числа»
# Напишите функцию square(number). Она принимает число и возвращает
# его квадрат. Вызовите функцию для чисел 5, 10 и 15, выводя результаты в
# консоль.

# def square(number):
#     return number ** 2
# print(square(5))
# print(square(8))
# print(square(11))
#
# Задача 3: «Проверка четности»
# Напишите функцию is_even(n), которая принимает целое число и
# возвращает True, если оно четное, и False, если нечетное.

# def is_even(n):
#     return n % 2 == 0
# print(is_even(4)) # True
# print(is_even(7)) # False
# print(is_even(18)) # True
#
# Задача 4: «Периметр прямоугольника»
# Напишите функцию calc_perimeter(a, b), которая принимает стороны
# прямоугольника и возвращает его периметр. Сохраните результат в
# переменную p и выведите её.
#
# def calc_perimeter(a, b):
#    return 2 * (a + b) # периметр прямоугольника
# perimetr = calc_perimeter(2, 3)
# print(perimetr)

# Задача 5: «Склеивание строк»
# Напишите функцию join_text(word1, word2), которая принимает два слова
# и возвращает их, соединенными через пробел.

# def join_text(word1, word2):
#     return word1 + word2
# print(join_text('Меня зовут', 'Михаил'))

# Задача 6: «Калькулятор скидок»
# Напишите функцию apply_discount(price, percent).
# Она принимает исходную цену и процент скидки. Функция должна возвращать новую цену.
# Дополнительно: если процент скидки больше 100 или меньше 0, функция должна возвращать текст "Ошибка".
#
# def apply_discount(price, percent):
#     if percent < 0 or percent > 100:
#         return 'Ошибка'
#
# # Задача 7: «Минимум из трех»
# # Напишите функцию min_of_three(a, b, c), которая принимает три числа и возвращает самое маленькое из них.
# # Использовать встроенную функцию min() нельзя.
#
def min_of_three(a, b, c):
    if a < b and a < c:
        return a
    elif b < c and b < a:
        return b
    elif c < a and c < b:
        return c

print(min_of_three(5, 2, 3))
#

