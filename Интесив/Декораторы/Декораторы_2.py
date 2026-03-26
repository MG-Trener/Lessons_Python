import time
def timing(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения функции: {end - start:.4f}')
    return wrapper

@timing
def slow_function():
    print('Функция запущена')
    summa = 0
    for i in range(100_000_000):
        summa += i
    print('Функция завершена')

slow_function()



