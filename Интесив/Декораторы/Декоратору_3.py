# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'Вызывается {func.__name__} с арргументами {args}, {kwargs}')
#         result = func(*args, **kwargs)
#         func(*args, **kwargs)
#         print(f'{func.__name__} вернула {result}')
#     return wrapper
#
# @decorator
# def add(a, b):
#     return a+b
# print(add(4,52))

# ====================
#
# 1. Декоратор проверки прав пользователя
# Напишите декоратор, который перед выполнением функции проверяет, является ли пользователь администратором


# def admin_decorator(func):
#     def wrapper(admin, *args, **kwargs):
#        if admin == 'admin':
#             return func(admin, *args, **kwargs)
#        else:
#            return 'У вас нет доступа'
#     return wrapper
#
# @admin_decorator
# def user(admin):
#     return 'Секретные данные'
#
# print(user('user_2'))
# print(user('admin'))

# =======================================
# Создание простого декоратора
# Напишите декоратор uppercase_decorator,
# который принимает функцию, возвращающую строку, и преобразует результат в верхний регистр.
# Примените его к функции, возвращающей ваше имя.


def up_word(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@up_word
def get_name():
    return 'Михаил'

print(get_name())