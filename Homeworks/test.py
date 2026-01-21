names = ["Alexander Pushkin", "Mikhail Lermontov", "Anton Chekhov"]

initials = [
    f"{n.split()[0][0]}.{n.split()[1][0]}."  # split -> ["Имя","Фамилия"], [0][0] первая буква имени, [1][0] первая буква фамилии
    for n in names                            # перебираем каждую строку списка
]
print(initials)