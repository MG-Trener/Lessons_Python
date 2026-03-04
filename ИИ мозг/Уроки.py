
import math

# Задача 2: Группы студентов
# Есть две группы студентов: одна изучает Python, другая - Java. Состав групп записан во множествах.
# Выведите общий список студентов (объединение).
# Найдите студентов, которые изучают оба языка (пересечение).
# Определите студентов, изучающих только Python.
# Пример данных:


python_group = {"Алиса", "Борис", "Катя"}
java_group = {"Катя", "Дима", "Елена"}

all_group = python_group | java_group
print(all_group)

group2 = python_group & java_group
print(group2)

group3 = python_group - java_group
print(group3)