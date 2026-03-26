# Задача 1: «Квадраты четных чисел»
# Создайте генераторное выражение, которое возводит в квадрат только четные числа от 1 до 10
#
# gen = (i**2 for i in range(11) if i % 2 == 0)
# print(list(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Задача 2: «Кричащие строки»
# Дан список слов ['python', 'is', 'cool']. Создайте генератор,
# который делает каждое слово заглавным и добавляет восклицательный знак.

word = ['python', 'is', 'cool']
word_2 = (i.upper() + '!' for i in word)
print(next(word_2))
print(next(word_2))
print(next(word_2))