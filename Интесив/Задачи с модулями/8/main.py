# Задача 8: «Расчет времени» (Модуль deadline.py)
# Что сделать: Используя datetime, создайте функцию days_until(target_date),
# которая принимает дату в формате "ГГГГ-ММ-ДД" и говорит,
# сколько дней осталось до неё. Пример вывода: До события осталось: 15 дней

from datetime import datetime

def days_until(date_str):
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    now = datetime.now()

    result_date = target_date - now
    return result_date

birthday = "2026-05-24"
print(f'да {days_until(birthday)}')