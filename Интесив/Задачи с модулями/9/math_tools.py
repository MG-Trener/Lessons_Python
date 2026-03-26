def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "_main_":
    print('Тут у нас модуль: ', get_factorial(6))