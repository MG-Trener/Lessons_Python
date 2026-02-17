# ==============================
# ЗАДАЧА 1: «Автоматическое письмо»
# ==============================

def create_email(username: str, domain: str = "gmail.com") -> str:
    # Функция принимает имя пользователя (строка)
    # domain — аргумент по умолчанию "gmail.com"
    # Возвращает строку (-> str)

    return f"{username}@{domain}"  # Формируем email через f-строку
print(create_email("mihagavr"))


# ==============================
# ЗАДАЧА 2: «Расчет площади»
# ==============================

def get_rectangle_area(width: float, height: float | None = None) -> float:
    # width — ширина (float)
    # height — высота (float или None)
    # Если height не передан (None), считаем квадрат

    if height is None:  # Проверяем, передали ли height
        return width * width  # Площадь квадрата
    else:
        return width * height  # Площадь прямоугольника
print(get_rectangle_area( 3, 5))


# ==============================
# ЗАДАЧА 3: «Повторитель строк»
# ==============================

def repeat_text(text: str, times: int = 2) -> str:
    # text — строка
    # times — сколько раз повторить (по умолчанию 2)

    return " ".join([text] * times) # [text] * times — создаёт список повторений
                                    # " ".join(...) — соединяет элементы через пробел
print(repeat_text("Astana", 3))

# ==============================
# ЗАДАЧА 4: «Конструктор цен»
# ==============================

def final_price(net_price: float, tax: float = 0.16) -> float:
    # net_price — цена без налога
    # tax — процент налога (по умолчанию 16%)

    return net_price * (1 + tax)
    # Добавляем налог к цене
print(final_price(500))


# ==============================
# ЗАДАЧА 5: «Статус заказа»
# ==============================

def update_status(order_id: int, status: str = "Обработка") -> dict[str, int | str]:
    # Возвращаем словарь с id и статусом

    return {
        "id": order_id,
        "status": status
    }
print(update_status(45, "Обработка"))
print(update_status(5, 'Онлайн'))


# ==============================
# ЗАДАЧА 6: «Проверка доступа»
# ==============================

def is_access_granted(user_role: str, min_level: str = "admin") -> bool:
    # Сравниваем роли
    return user_role == min_level
    # Если совпадают — True, иначе False
print(is_access_granted('admin'))
# ==============================
# ЗАДАЧА 7: «Калькулятор ИМТ»
# ==============================

def calculate_bmi(weight: float, height: float) -> float:
    # Формула BMI = weight / height^2
    bmi = weight / (height ** 2)  # Возведение в степень **
    return round(bmi, 1)  # Округление до 1 знака
print(calculate_bmi(20, 2))


# ==============================
# ЗАДАЧА 8: «Фильтр списка»
# ==============================

def filter_list(numbers: list[int], threshold: int = 0) -> list[int]:
    # Возвращаем новый список с числами больше threshold

    return [num for num in numbers if num > threshold]
    # List comprehension
print(filter_list([1, 2, 3, 4, 5], 3))


# ==============================
# ЗАДАЧА 9: «Создание заголовка»
# ==============================

def make_header(text: str, level: int = 1) -> str:
    # Формируем HTML заголовок

    return f"<h{level}>{text}</h{level}>"
print(make_header('Тема', 2))


# ==============================
# ЗАДАЧА 10: «Логическая бомба»
# ==============================

def check_coordinates(x: int, y: int, max_val: int = 100) -> bool:
    # Проверяем, что оба числа в диапазоне от 0 до max_val включительно

    return 0 <= x <= max_val and 0 <= y <= max_val
    # Используем логическое И (and)
print(check_coordinates(1, 101))
print(check_coordinates(1, 100))
print(check_coordinates(200, 100))