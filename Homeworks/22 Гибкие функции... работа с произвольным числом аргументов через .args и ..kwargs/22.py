# Задача 3: «Описание товара»
# Напишите функцию describe_item(title, *features). Первый аргумент - название товара.
# Остальные (*kwargs) - его характеристики.
# Пример вызова: describe_item("Laptop", brand="Apple", ram="16GB", cpu="M2").
# Функция должна напечатать название и перечислить все характеристики.
def describe_item(title, **features):
    print(title)
    for key, value in features.items():
        print(key, value)

describe_item("Laptop", brand="Apple", ram="16GB", cpu="M2")