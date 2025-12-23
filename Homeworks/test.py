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