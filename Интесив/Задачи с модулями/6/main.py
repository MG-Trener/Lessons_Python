# Задача 6: «Валидатор паролей» (Модуль security.py)
# Что сделать: Напишите функцию validate(password), которая возвращает True,
# если в пароле больше 6 символов и есть хотя бы одна цифра. Пример вывода: Пароль 'qwerty' валиден? False

from security import validate

print(validate('qwertywqw'))