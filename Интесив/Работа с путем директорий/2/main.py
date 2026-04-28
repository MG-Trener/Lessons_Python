import os

# os.path

my_path = "Новая папка/text.txt"
print(os.path.abspath(my_path))
print(os.path.dirname(my_path))
print(os.path.basename(my_path))
print(os.path.splitext(my_path))
print(os.path.splitext(my_path)[-1])

full_path = ['c:', 'users', 'user', 'file.txt']
print(os.path.join(*full_path))