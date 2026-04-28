import os

print(os.listdir())

folder = input("Назовите новую папку: ")

def make_dir():

    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Папка '{folder}' создана")
    else:
        print(f"Папка '{folder}' уже существует")

# удаляет файл, который ест ьв директории
if os.path.exists(folder):
    os.remove(folder)
    print('Файл удален')
else:
    print('Такой файла не существует')