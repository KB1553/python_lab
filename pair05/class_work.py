# Приклад 1. Функція без параметрів
def say_hello():
    print("Привіт, Python!")

say_hello()


# Приклад 2. Функція з параметром
def greet(name):
    print(f"Привіт, {name}!")

greet("Ivan")


# Приклад 3. Функція з return
def area_rectangle(a, b):
    return a * b

area = area_rectangle(7, 4)
print("Площа:", area)


# Приклад 4. print() і return
def square_print(x):
    print(x * x)

def square_return(x):
    return x * x

square_print(5)
result = square_return(5)
print("Результат можна використати:", result + 10)


# Приклад 5. Параметр за замовчуванням
def greet_default(name, message="Привіт"):
    print(f"{message}, {name}!")

greet_default("Anna")
greet_default("Ivan", "Добрий день")


# Приклад 6. Іменовані аргументи
def student_info(name, group, grade):
    print(f"{name}: група {group}, оцінка {grade}")

student_info(grade=11, name="Anna", group="10-IT")


# Приклад 7. Повернення двох значень
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([7, 2, 15, 4, 9])
print("Min:", minimum)
print("Max:", maximum)


# Приклад 8. Функція перевірки значення
def is_valid_grade(grade):
    return 1 <= grade <= 12

grade = int(input("Оцінка: "))
if is_valid_grade(grade):
    print("Коректна оцінка")
else:
    print("Помилка")


# Приклад 9. Кілька функцій для аналізу списку
def average(numbers):
    return sum(numbers) / len(numbers)

def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

numbers = [4, -2, 8, 0, 5]
print("Середнє:", average(numbers))
print("Додатних:", count_positive(numbers))


# Приклад 10. *args
def total_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(total_sum(5, 10))
print(total_sum(1, 2, 3, 4, 5))


# Приклад 11. main() координує програму
def area_rect(a, b):
    return a * b

def main11():
    width = float(input("Ширина: "))
    height = float(input("Висота: "))
    result = area_rect(width, height)
    print("Площа:", result)

main11()


# Приклад 12. Декомпозиція програми
def input_grades():
    return [10, 8, 12, 9, 11]

def calc_average(grades):
    return sum(grades) / len(grades)

def best_grade(grades):
    return max(grades)

def print_report(grades):
    print("Оцінки:", grades)
    print("Середній бал:", round(calc_average(grades), 2))
    print("Найкраща оцінка:", best_grade(grades))

def main12():
    grades = input_grades()
    print_report(grades)

main12()