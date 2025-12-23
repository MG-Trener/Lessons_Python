# ============================================================
# Задача 1: Детектор анаграмм
# Проверяем, можно ли из одной строки собрать другую
# ============================================================

s1 = "listen"
s2 = "silent"

# Приводим строки к одному виду и сортируем буквы
sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)

# Если отсортированные списки равны — это анаграммы
if sorted_s1 == sorted_s2:
    print("Строки являются анаграммами")
else:
    print("Строки не являются анаграммами")


# ============================================================
# Задача 2: CamelCase → snake_case
# Нужно вставить _ перед заглавными буквами и привести к lower
# ============================================================

camel = "myVariableName"
snake = ""                        # Результирующая строка

for char in camel:                # Перебираем каждый символ
    if char.isupper():            # Если буква заглавная
        snake += "_" + char.lower()  # Добавляем "_" и строчную букву
    else:
        snake += char             # Иначе просто добавляем символ

print(snake)


# ============================================================
# Задача 3: Самое длинное слово в тексте
# ============================================================

text = "Python делает анализ текста удобным"
words = text.split()              # Разбиваем строку на слова

longest_word = ""                 # Здесь будем хранить самое длинное слово

for word in words:
    if len(word) > len(longest_word):
        longest_word = word       # Запоминаем более длинное слово

print(longest_word)
print(len(longest_word))


# ============================================================
# Задача 4: Валидатор супер-пароля
# ============================================================

password = "Secure@123"
errors = []                       # Список недостающих условий

if len(password) < 8:
    errors.append("длина меньше 8")

if not any(ch.isupper() for ch in password):
    errors.append("нет заглавной буквы")

if not any(ch.isdigit() for ch in password):
    errors.append("нет цифры")

if not any(ch in "!@#" for ch in password):
    errors.append("нет спецсимвола")

if not errors:
    print("Пароль принят")
else:
    print("Пароль слабый, не хватает:", ", ".join(errors))


# ============================================================
# Задача 5: Переворот слов, но не предложения
# ============================================================

sentence = "Python это круто"
words = sentence.split()          # Разбиваем на слова

reversed_words = []               # Список перевёрнутых слов

for word in words:
    reversed_words.append(word[::-1])  # Переворачиваем каждое слово

result = " ".join(reversed_words) # Собираем обратно строку
print(result)


# ============================================================
# Задача 6: Сжатие строки (RLE)
# ============================================================

data = "aaabbccccd"
compressed = ""
count = 1

for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        count += 1                # Увеличиваем счётчик
    else:
        compressed += data[i - 1] + str(count)
        count = 1                 # Сбрасываем счётчик

compressed += data[-1] + str(count)  # Добавляем последний символ
print(compressed)


# ============================================================
# Задача 7: Удаление лишних пробелов (без replace)
# ============================================================

text = "Python     очень      удобный     язык"
clean_text = ""
prev_space = False                # Флаг предыдущего пробела

for char in text:
    if char == " ":
        if not prev_space:
            clean_text += char
        prev_space = True
    else:
        clean_text += char
        prev_space = False

print(clean_text)


# ============================================================
# Задача 8: Шифр Цезаря
# ============================================================

message = "abcxyz"
k = 3
encrypted = ""

for char in message:
    new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    encrypted += new_char

print(encrypted)


# ============================================================
# Задача 9: Поиск подстроки без find() и in
# ============================================================

text = "Программирование"
substr = "мир"
index = -1

for i in range(len(text) - len(substr) + 1):
    if text[i:i + len(substr)] == substr:
        index = i
        break

print(index)


# ============================================================
# Задача 10: Форматирование текста по ширине
# ============================================================

words = ["Python", "—", "очень", "гибкий", "язык"]
N = 30

text_len = sum(len(word) for word in words)  # Сумма длин слов
spaces_needed = N - text_len                 # Сколько пробелов нужно
gaps = len(words) - 1                        # Количество промежутков

base_space = spaces_needed // gaps            # Минимум пробелов
extra = spaces_needed % gaps                  # Лишние пробелы

result = ""

for i in range(len(words)):
    result += words[i]
    if i < gaps:
        result += " " * (base_space + (1 if i < extra else 0))

print(result)
print(len(result))
