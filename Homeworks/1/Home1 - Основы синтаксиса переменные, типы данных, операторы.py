# 1 задача
# Исходные значения
config_role_a = "Администратор"
config_role_b = "Гость"
# Обмен значениями
config_role_a, config_role_b = config_role_b, config_role_a
# Вывод результата
print("config_role_a", config_role_a)
print("config_role_b:", config_role_b)

#########################################

# 2 задача
quiz_score = 15
max_score = 20
result = max_score - quiz_score
print("Потеряно", result, "баллов")  #вывод
percent = quiz_score * 100 / max_score
print("Процент", percent, "%")
result_delenie = max_score // 3
print("Целочисленное деление", result_delenie)
result_delenie_part = quiz_score % 4
print("Остаток", result_delenie_part)
stepen = quiz_score ** 2
print("Степень", stepen)

##############################

# 3 задача
# Объявляем переменные разных типов
lesson_time = 20  # int
pi_value = 3.14  # float
error_code = "Ошибка в коде"  # str
is_online = True  # bool
# Выводим значения и типы данных
print(lesson_time, type(lesson_time))
print(pi_value, type(pi_value))
print(error_code, type(error_code))
print(is_online, type(is_online))

##############################

# 4 задача
#Задаем переменные
progress_client_a = 0.75  # (прогресс первого клиента)
progress_client_b = 0.82  # (прогресс второго клиента)
#Сравниваем и выводим результат
result_srav = progress_client_a < progress_client_b #True
result_srav2 = progress_client_a > progress_client_b
result_srav3 = progress_client_a == progress_client_b
result_srav4 = progress_client_a != progress_client_b
print("0.75 меньше 0.82 это", result_srav)
print("0.75 больше 0.82 это", result_srav2)
print("0.75 равно 0.82 это", result_srav3)
print("0.75 не равно 0.82 это", result_srav4)

################################

# 5 задача
current_age = 41
is_working_age = current_age > 18 and current_age < 65
is_extreme_age = current_age <  65 and current_age > 65
is_not_child = not (current_age < 65)
print(is_not_child, type(is_not_child))
print(current_age, type(current_age))
print(is_working_age, type(is_working_age))


# ================================
# ЗАДАЧА 5: Критерии допуска
# ================================

current_age = 40  # задаем свой возраст

# Проверяем, является ли возраст трудоспособным
is_working_age = current_age > 18 and current_age < 65
# Проверяем, относится ли возраст к "крайним" (дети или пожилые)
is_extreme_age = current_age < 18 or current_age > 65
# Проверяем, что человек НЕ ребенок младше 12
is_not_child = not (current_age < 12)

print("=== Задача 5 ===")
print("is_working_age:", is_working_age)
print("is_extreme_age:", is_extreme_age)
print("is_not_child:", is_not_child)
print()

# ================================
# ЗАДАЧА 6: Расчет 3D-модели
# ================================

length = 5
width = 3
height = 2

# Площадь основания
base_area = length * width
# Объем параллелепипеда
volume = length * width * height
# Периметр основания
base_perimeter = 2 * (length + width)

print("=== Задача 6 ===")
print("Площадь основания:", base_area)
print("Объем:", volume)
print("Периметр основания:", base_perimeter)
print()

# ================================
# ЗАДАЧА 7: Конвертер метрик
# ================================

distance_meters = 5.5  # расстояние в метрах

# Переводим в сантиметры
distance_cm = distance_meters * 100
# Переводим в километры
distance_km = distance_meters / 1000
# Проверяем, считается ли расстояние "длинной поездкой"
is_long_trip = distance_km >= 1

print("=== Задача 7 ===")
print("distance_cm:", distance_cm)
print("distance_km:", distance_km)
print("is_long_trip:", is_long_trip)
print()

# ================================
# ЗАДАЧА 8: Дублирование текста
# ================================

word_a = "Python"
word_b = "Code"

# Повторяем слово Python три раза
phrase_a = word_a * 3
# Склеиваем слово Code два раза
phrase_b = word_b + word_b
# Сравниваем их лексикографически (по алфавиту)
is_lexicographically_bigger = phrase_a > phrase_b

print("=== Задача 8 ===")
print("phrase_a:", phrase_a)
print("phrase_b:", phrase_b)
print("is_lexicographically_bigger:", is_lexicographically_bigger)
print()

# ================================
# ЗАДАЧА 9: Фильтрация данных
# ================================

data_rows = 150
data_quality = 0.9
has_errors = True  # есть ошибки

# Готовы ли данные к анализу:
# только если строк больше 100, качество > 0.8 и ошибок нет
is_ready_for_analysis = (data_rows > 100 and data_quality > 0.8) and not has_errors

print("=== Задача 9 ===")
print("is_ready_for_analysis:", is_ready_for_analysis)
print()

# ================================
# ЗАДАЧА 10: Формула сложного индекса
# ================================

base_value = 5.5
divider = 3

# Возводим base_value в квадрат
step_1 = base_value ** 2
# Целочисленно делим результат на divider
index_result = step_1 // divider
# Находим остаток от деления index_result на 2
remainder_check = index_result % 2
# Проверяем условие: index_result > 10 ИЛИ остаток равен 0
is_valid_index = index_result > 10 or remainder_check == 0

print("=== Задача 10 ===")
print("index_result:", index_result)
print("is_valid_index:", is_valid_index)
