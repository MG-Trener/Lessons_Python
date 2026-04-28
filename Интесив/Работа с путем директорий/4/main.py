# Задача 2.
# Создайте файл config.txt внутри папки Settings
# (если папки нет - создайте). Запишите в него строку "version=1.0"

import os

directory = 'Setting'

if not os.path.exists(directory):
    os.mkdir(directory)
    print(f'Папка {directory} создана')
else:
    print('Папка уже существует')

with open(os.path.join(directory, 'config.txt'), 'w', encoding='utf-8') as file:
    file.write('version=1.0')

