# Задача 1.
# Напишите скрипт, который выводит текущую директорию, создаёт папку
# MyProject и внутри неё - папку reports.
import os  # модуль для работы с файловой системой

# Выводим текущую директорию
print("Текущая директория:", os.getcwd())

# Имя основной папки проекта
folder_name = "MyProject"

# Формируем путь к вложенной папке Reports
# Пока это относительный путь: MyProject/Reports
reports = os.path.join(folder_name, "Reports")


# Проверяем, существует ли папка MyProject
if not os.path.exists(folder_name):  # если нет
    os.mkdir(folder_name)  # создаём папку MyProject
    print(f"Папка '{folder_name}' создана")
else:
    print(f"Папка '{folder_name}' уже существует")


# Теперь проверяем папку Reports внутри MyProject
if not os.path.exists(reports):  # если нет
    os.mkdir(reports)  # создаём вложенную папку
    print(f"Папка 'Reports' создана внутри '{folder_name}'")
else:
    print(f"Папка 'Reports' уже существует")

with open(reports, "w", encoding="utf-8") as f: