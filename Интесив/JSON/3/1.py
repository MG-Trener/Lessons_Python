# Задача 5: “Поиск пользователя по имени”
# Дано: Файл users.json:
# [
#  {"name": "Алихан", "age": 25},
#  {"name": "Бауыржан", "age": 30},
#  {"name": "Айгерим", "age": 22}
# ]
#
# Задача:
# Запросить имя у пользователя
# Найти этого человека в JSON
# Вывести его возраст
# Если нет — вывести "Пользователь не найден"
import json
user_name = input('Как вас зовут? ')

with open('users3.json', 'r', encoding='utf-8') as read_file:
    users = json.load(read_file)

is_found = False
for user in users:
    if user['name'] == user_name:
        is_found = True
        print(user['name'], user['age'])
        break
if not is_found:
    print('Пользователь не найден')