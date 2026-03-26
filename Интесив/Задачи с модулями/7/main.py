# Задача 7: «Системный информер» (Модуль sys_info.py)
# Что сделать: Используя стандартный модуль os, создайте функцию get_current_folder(),
# которая возвращает название папки, в которой запущен скрипт. Пример вывода: Вы работаете в папке: MyProject

import os

def get_current_folder():
    return os.path.basename(os.getcwd())

print(f"Вы работаете в папке: {get_current_folder()}")