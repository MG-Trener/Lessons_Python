# Условие: Напишите функцию check_temperature(t).
# Если температура ниже -50 или выше 50, вызывайте ValueError с текстом "Критическая температура!".

# def check_temperature(t):
#     if t < -50 or t > 50:
#         raise ValueError ('Критическая температура!')
#     return t
# try:
#     print(check_temperature(50))
# except ValueError as error:
#     print(f'{error}')

# Условие: Функция only_even(n) должна принимать только четные (числа.
# Если)    передано    нечетное — raise TypeError("Только четные числа!").

# def only_even(n):
#     if n % 2 != 0:
#         return TypeError('Только четные числа!')
#     return n //2
# try:
#     print(only_even(4))
# except TypeError as error:
#     print(f'{error}')
#
#     Условие: Функция    set_grade(score).Если    оценка    не    входит    в    диапазон
#     от    1    до    5, вызвать    ValueError.Если    оценка — не    целое    число, вызвать    TypeError.

# def set_grade(score):
#     if not isinstance(score, int):
#         raise TypeError('Оценка должна быть целым числом')
#     else:
#         if score < 1 or score > 5:
#             raise ValueError('Оценки должны быть от 1 до 5')
#     return score
# try:
#     print(set_grade(5))
# except (TypeError, ValueError) as error:
#     print(error)
#
# Условие: Создайте функцию withdraw(amount).
# Если amount (сумма для снятия) меньше или равна 0, вызывайте ValueError с текстом "Сумма должна быть положительной".

# def withdraw(amount):
#     if amount <= 0:
#         raise ValueError('Сумма должна быть положительной')
#     return amount
#
# try:
#     print('Успешное снятие', withdraw(10), 'тенге')
# except ValueError as e:
#     print(e)
#
# Условие: Функция check_pin(pin).
# Если pin не равен "1234", вызывайте PermissionError (или ValueError) с текстом "Неверный ПИН-код".
# После 3 попыток программа должна закрыться (используйте цикл).

def check_pin(pin):
    if pin != '1234':
        raise PermissionError('Неверный ПИН-код')
    return 'Доступ разрешен'
for i in range(3):

    try:
        user_pin = str(input('Введите PIN: '))
        print(check_pin(user_pin))
        break
    except PermissionError as e:
        print(e, f'Оcталось попыток: {2-i}')