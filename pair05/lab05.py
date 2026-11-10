# Завдання 1. Площі геометричних фігур
def area_circle(r):
    return 3.14159 * r * r

def area_rectangle(w, h):
    return w * h

def area_triangle(b, h):
    return 0.5 * b * h

def task1():
    fig = input("Фігура: ").strip().lower()
    if fig == "прямокутник":
        w = float(input("Ширина: "))
        h = float(input("Висота: "))
        print("Площа прямокутника:", area_rectangle(w, h))
    elif fig == "круг":
        r = float(input("Радіус: "))
        print("Площа круга:", area_circle(r))
    elif fig == "трикутник":
        b = float(input("Основа: "))
        h = float(input("Висота: "))
        print("Площа трикутника:", area_triangle(b, h))


# Завдання 2. Функції для аналізу числа
def is_prime(n):
    if n < 2:
        return "ні"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "ні"
    return "так"

def divisors(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res

def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def task2():
    n = int(input("N = "))
    print("Просте число:", is_prime(n))
    print("Дільники:", divisors(n))
    print("Сума цифр:", digit_sum(n))


# Завдання 3. Звіт за списком оцінок
def average(grades):
    return sum(grades) / len(grades)

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    count = 0
    for g in grades:
        if g > value:
            count += 1
    return count

def task3():
    grades = [10, 8, 12, 9, 11]
    value = int(input("Поріг: "))
    print("Оцінки:", grades)
    print("Середній бал:", average(grades))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print(f"Вище {value}:", count_above(grades, value))


# Завдання 4. Перевірка надійності пароля
def check_length(p):
    return len(p) >= 8

def check_digit(p):
    for ch in p:
        if ch.isdigit():
            return True
    return False

def check_upper(p):
    for ch in p:
        if ch.isupper():
            return True
    return False

def check_lower(p):
    for ch in p:
        if ch.islower():
            return True
    return False

def check_special(p):
    for ch in p:
        if not ch.isalnum():
            return True
    return False

def validate_password(password):
    errors = []
    if not check_length(password):
        errors.append("мінімальна довжина менше 8 символів")
    if not check_digit(password):
        errors.append("немає цифри")
    if not check_upper(password):
        errors.append("немає великої літери")
    if not check_lower(password):
        errors.append("немає малої літери")
    if not check_special(password):
        errors.append("немає спеціального символу")
    
    return errors

def task4():
    password = input("Password: ")
    errors = validate_password(password)
    if len(errors) == 0:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано:", ", ".join(errors))


def main():
    print("=== Завдання 1 ===")
    task1()
    print("\n=== Завдання 2 ===")
    task2()
    print("\n=== Завдання 3 ===")
    task3()
    print("\n=== Завдання 4 ===")
    task4()

if __name__ == "__main__":
    main()