import csv

# data = [
#     ['Name', 'Age',],
#     ['John', 10,],
#     ['Mary', 20,],
# ]
# #создаем файл и записываем данные
# with open('students.csv', 'w', encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)

total = 0
with open('students.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        age = int(row[1])
        total = age + total
print(total)
