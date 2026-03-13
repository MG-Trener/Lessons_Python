# Задача 1: «Конвертер валют» (Модуль currency.py)
# Что сделать: Создайте модуль currency.py, который содержит переменную курса USD_TO_KZT = 493 и функцию convert_to_kzt(dollars).
# Пример вывода в main.py: 100 долларов - это 49300 тенге

USD_TO_KZT = 493
def convert_to_kzt(dollars):
    return dollars * USD_TO_KZT