# Приклад 1. int(input()) і ValueError
try:
    number = int(input("Число: "))
    print("Ви ввели:", number)
except ValueError:
    print("Помилка: введіть ціле число.")

# Приклад 2. Ділення і ZeroDivisionError
try:
    a = float(input("A: "))
    b = float(input("B: "))
    print("Результат:", a / b)
except ValueError:
    print("Потрібно ввести числа.")
except ZeroDivisionError:
    print("На нуль ділити не можна.")

# Приклад 3. IndexError
numbers = [10, 20, 30]
try:
    index = int(input("Індекс: "))
    print(numbers[index])
except ValueError:
    print("Індекс повинен бути цілим числом.")
except IndexError:
    print("Такого індексу немає.")

# Приклад 4. KeyError і get()
prices = {
    "apple": 35,
    "banana": 52
}
product = input("Товар: ")
try:
    print("Ціна:", prices[product])
except KeyError:
    print("Товар не знайдено.")
print("Через get():", prices.get(product, "немає даних"))

# Приклад 5. FileNotFoundError
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл data.txt не знайдено.")

# Приклад 6. Кілька except
try:
    a = int(input("A: "))
    b = int(input("B: "))
    result = a / b
except ValueError:
    print("A і B повинні бути цілими числами.")
except ZeroDivisionError:
    print("B не може дорівнювати нулю.")
else:
    print("Результат:", result)

# Приклад 7. else після успішної операції
try:
    age = int(input("Вік: "))
except ValueError:
    print("Некоректне число.")
else:
    print("Дані прийнято.")
    print("Через 5 років:", age + 5)

# Приклад 8. finally
try:
    file = open("data.txt", "r", encoding="utf-8")
    print(file.read())
except FileNotFoundError:
    print("Файл не знайдено.")
else:
    file.close()
finally:
    print("Спробу роботи з файлом завершено.")

# Приклад 9. safe_int_input()
def safe_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Введіть ціле число.")

count = safe_int_input("Кількість: ")
print("Кількість:", count)

# Приклад 10. raise ValueError
def check_age(age):
    if age < 0 or age > 120:
        raise ValueError("Некоректний вік.")
    return age

try:
    age = int(input("Вік: "))
    check_age(age)
    print("Вік прийнято.")
except ValueError as error:
    print("Помилка:", error)

# Приклад 11. Перевірка оцінки 1..12
def input_grade():
    while True:
        try:
            grade = int(input("Оцінка 1..12: "))
            if grade < 1 or grade > 12:
                raise ValueError("Оцінка поза діапазоном.")
            return grade
        except ValueError as error:
            print("Помилка:", error)

grade = input_grade()
print("Прийнято:", grade)

# Приклад 12. Надійне меню програми
def show_menu():
    print("1 - Додати")
    print("2 - Переглянути")
    print("0 - Вихід")

while True:
    show_menu()
    try:
        choice = int(input("Ваш вибір: "))
        if choice not in [0, 1, 2]:
            raise ValueError("Невідомий пункт меню.")
    except ValueError as error:
        print("Помилка:", error)
        continue

    if choice == 0:
        print("Завершення програми.")
        break
    elif choice == 1:
        print("Додавання даних...")
    elif choice == 2:
        print("Перегляд даних...")