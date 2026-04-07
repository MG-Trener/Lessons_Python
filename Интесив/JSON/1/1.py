# Задача 3: “Добавление нового пользователя”
# Дано: Файл users.json:
# [
#   {"name": "Алихан", "age": 25},
#   {"name": "Бауыржан", "age": 30}
# ]
# Задача:
# Запросить у пользователя имя и возраст
# Добавить нового пользователя в JSON
# Сохранить файл
import json
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

with open('user.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

dict_user = {
    'name': user_name,
    'age': user_age
}

data.append(dict_user)

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
print('Программа завершена')



