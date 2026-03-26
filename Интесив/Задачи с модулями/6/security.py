# Задача 6: «Валидатор паролей» (Модуль security.py)
# Что сделать: Напишите функцию validate(password), которая возвращает True,
# если в пароле больше 6 символов и есть хотя бы одна цифра. Пример вывода: Пароль 'qwerty' валиден? False

def validate(password: str) -> bool:
    if len(password) > 6 and any(i.isdigit() for i in password):
        return True
    else:
        return False