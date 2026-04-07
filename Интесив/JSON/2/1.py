# Задача 4: “Подсчёт общей суммы заказов”
# Дано: Файл orders.json:
# # [
# #  {"product": "Телефон", "price": 150000},
# #  {"product": "Наушники", "price": 30000},
# #  {"product": "Клавиатура", "price": 20000}
# # ]
#
# Задача: Посчитать и вывести общую сумму всех заказов

import json

with open('orders.json', 'r', encoding='utf-8') as file:
    products = json.load(file)
    print(products)

all_price = 0

for product in products:
    all_price += product['price']

print(all_price)