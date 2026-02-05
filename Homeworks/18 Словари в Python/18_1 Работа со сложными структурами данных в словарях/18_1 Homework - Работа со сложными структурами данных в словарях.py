# # ЗАДАЧА 1. Расписание занятий
# # создаём словарь, где ключ — день недели, значение — список уроков
#
schedule = {
    "Понедельник": ["Математика", "Физика"],
    "Вторник": ["История", "Литература"]
}
print('\nПервое расписание', schedule)
schedule["Понедельник"].append("Программирование") # Добавляем
print('Дополненное расписание', schedule)

# # ЗАДАЧА 2. Мини-склад
# # Создаём словарь склада: ключ — название товара, значение — кортеж (цена, количество)

warehouse = {
    "Монитор": (120000, 5),
    "Клавиатура": (15000, 20)
}
print('\nЧто на складе: ', warehouse)
print('Цена монитора', warehouse["Монитор"][0])

# # # ЗАДАЧА 3. Профиль в соцсетях
# #
user_profile = {
    "name": "Alex",
    "friends": ["Ivan", "Maria", "John"]
}
print('\nПрофиль друзей: ', user_profile)
# user_profile["friends"].remove("Ivan")
user_profile["friends"].pop() # Удаляем последнее имя из списка друзей
print('Обновленный профиль друзей: ', user_profile)

# ЗАДАЧА 4. Справочник столиц
# создаём список, содержащий два словаря
countries = [
    {"country": "Kazakhstan", "capital": "Astana"},
    {"country": "France", "capital": "Paris"}
]
print('\nСписок словарей', countries)
second_capital = countries[1]["capital"] # индекс 1 в списке
print('Столица второго словаря: ', second_capital)

# ЗАДАЧА 5. Координаты склада
# Создаём словарь, где ключ — кортеж координат, значение — объект
map_objects = {
    (10, 20): "Склад",
    (5, 8): "Магазин",
    (8, 15): "Отдел"
}
print('\n', map_objects)
has_object = (10, 20) in map_objects # Проверяем True/False, существует ли объект по координатам (10, 20)
print(has_object)

# ЗАДАЧА 6. Аналитика продаж
# Список словарей с данными о продажах
sales = [
    {"item": "Apple", "amount": 500},
    {"item": "Milk", "amount": 300},
    {"item": "Apple", "amount": 200}
]
print('\n Все словари: ', sales)
apple_sales_total = 0 # Суммируем amount только для товаров с названием "Apple"
for sale in sales:
    if sale["item"] == "Apple":
        apple_sales_total += sale["amount"]
print('Сумма всех яблок: ', apple_sales_total)

# ЗАДАЧА 7. Глубокое обновление (JSON-style)
# Структура компании
company = {
    "HR": {
        "employees": ["Alikhan", "Elena"],
        "office": 101
    },
    "IT": {
        "employees": ["Boris", "Samat"],
        "office": 102
    }
}
print('\nПервый состав', company)
company["IT"]["employees"].append("Aisulu") # Добавляем нового сотрудника "Aisulu" в отдел IT
print('Второй состав',company)

# ЗАДАЧА 8. Фильтр по GPA
# Список студентов с оценками
students = [
    {"name": "Aruzhan", "grades": [90, 80, 100]},
    {"name": "Igor", "grades": [70, 60, 65]}
]
good_students = [] # Создаём список имён студентов со средним баллом выше 75

for student in students:
    average = sum(student["grades"]) / len(student["grades"])
    if average > 75:
        good_students.append(student["name"])



# ЗАДАЧА 9. Иерархия городов
# Словарь областей и городов Казахстана
kazakhstan = {
    "Алматинская область": {
        "Алматы": 2000000,
        "Конаев": 70000
    },
    "Акмолинская область": {
        "Кокшетау": 150000
    }
}

# Считаем общее население городов Алматинской области
total_population = sum(kazakhstan["Алматинская область"].values())


# ЗАДАЧА 10. Валидация системы
# Кортеж конфигураций
CONFIG = (
    {"port": 8080, "status": "on"},
    {"port": 3000, "status": "off"}
)

# Проверяем, у всех ли словарей port больше 1024
all_ports_valid = all(config["port"] > 1024 for config in CONFIG)
