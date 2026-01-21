## Задача 1. Извлечение инициалов

names = ["Alexander Pushkin", "Mikhail Lermontov", "Anton Chekhov"]

initials = [
    f"{n.split()[0][0]}.{n.split()[1][0]}."  # split -> ["Имя","Фамилия"], [0][0] первая буква имени, [1][0] первая буква фамилии
    for n in names                            # перебираем каждую строку списка
]
print(initials)
## Задача 2. Поиск общих элементов (без множеств)

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common = [
    x for x in list_a     # перебираем элементы первого списка
    if x in list_b        # оставляем только те, которые есть во втором списке
]
print(common)
## Задача 3. Фильтрация email по домену

emails = ["test@gmail.com", "work@mail.ru", "info@gmail.com", "study@yandex.ru"]
gmail = [
    e for e in emails                 # перебираем все email
    if e.endswith("@gmail.com")       # проверяем окончание строки
]
print(gmail)
## Задача 4. Простые числа

primes = [
    n for n in range(2, 101)                                   # числа от 2 до 100
    if all(n % d != 0 for d in range(2, int(n**0.5) + 1))      # нет делителей от 2 до √n
]
print(primes)
## Задача 5. Удаление гласных (вложенный генератор)

sentences = ["Python is great", "I love code"]
no_vowels = [
    ''.join(
        c for c in s                    # перебираем символы строки
        if c.lower() not in "yaeiou"     # исключаем гласные
    )
    for s in sentences                  # перебираем предложения
]
print(no_vowels)
## Задача 6. Шифр Цезаря (+3)

text = "abcxyz"
print(ord('a'))
cipher = ''.join( # join склеивает все символы
    chr((ord(c) - 97 + 3) % 26 + 97)    # ord -> сдвиг -> зацикливание -> chr
    for c in text                       # перебор символов строки
)
print(cipher)

## Задача 7. Группировка по чётности

nums = [1, 2, 3, 4, 5, 6]
grouped = [
    [n for n in nums if n % 2 == 0],    # список чётных чисел
    [n for n in nums if n % 2 != 0]     # список нечётных чисел
]
print(grouped)
## Задача 8. Пары с суммой X

nums = [2, 4, 6, 8, 5, 5]
x = 10
pairs = list({
    tuple(sorted((nums[i], nums[j])))          # сортируем пару для уникальности
    for i in range(len(nums))                  # первый индекс
    for j in range(i + 1, len(nums))           # второй индекс (i < j)
    if nums[i] + nums[j] == x                  # сумма равна X
})
print(pairs)
## Задача 9. Нормализация данных

data = [10, 15, 20, 50, 100]
max_data = max(data) # записываем максимальное значение в новую переменную
normalized = [
    x / max_data     # делим каждый элемент на максимальное значение списка
    for x in data
]
print(normalized)
## Задача 10. Анаграммы

target = "listen"
words = ["silent", "google", "enlist", "apple"]
anagrams = [
    w for w in words              # перебираем слова
    if sorted(w) == sorted(target)  # анаграммы имеют одинаковый набор букв
]
print(anagrams)
print(sorted('listen'))
print(sorted('silent'))
print(sorted('enlist'))
