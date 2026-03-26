# def test(name, age, user):
#     if user == 'admin':
#         return (f'{name} is {age} years old')
#     else:
#         return f'У вас нет доступа'
#
# print(test('Михаил', '41', 'adminw'))


def decorator(func):
    def wrapper():
        print('Какое то сообщение перед выполеннием функции')
        func()
        print('Сообщение после выполнения функции')
    return wrapper

@decorator
def say_hello():
    print('hello')
say_hello()


@decorator
def add():
    print(f'a+b=', 4+5)

add()