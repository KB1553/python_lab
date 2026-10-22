# Приклад 1. Статистика списку оцінок
grades = [10, 8, 12, 9, 11]
print("Min:", min(grades))
print("Max:", max(grades))
print("Сума:", sum(grades))
print("Середнє:", sum(grades) / len(grades))

# Приклад 2. Додавання, видалення та сортування
numbers = [5, 2, 9, 1]
numbers.append(7)
numbers.remove(2)
numbers.sort()
print(numbers)

# Приклад 3. Фільтрація у новий список
numbers = [12, -3, 4, -7, 10, 5]
positive = []
for number in numbers:
    if number > 0:
        positive.append(number)
print(positive)

# Приклад 4. Кортеж координат і розпакування
point = (15, -4)
x, y = point
print("x:", x)
print("y:", y)

# Приклад 5. Видалення дублікатів через set
names = ["Ivan", "Anna", "Ivan", "Olha", "Anna"]
unique_names = set(names)
print(unique_names)

# Приклад 6. Спільні елементи двох множин
math = {"Ivan", "Anna", "Olha"}
python = {"Anna", "Maksym", "Ivan"}
print("Спільні:", math & python)
print("Тільки math:", math - python)
print("Усі:", math | python)

# Приклад 7. Словник товарів
prices = {"bread": 35, "milk": 48}
prices["cheese"] = 120
prices["bread"] = 38
print(prices)

# Приклад 8. Перебір items()
prices = {"bread": 38, "milk": 48, "cheese": 120}
for product, price in prices.items():
    print(product, "-", price, "грн")

# Приклад 9. Учень -> список оцінок
students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10]
}
print(students["Anna"])

# Приклад 10. Середній бал кожного учня
students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10]
}
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, round(average, 2))

# Приклад 11. Пошук найкращого результату
students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10],
    "Olha": [11, 12, 12]
}
best_name = ""
best_average = 0
for name, grades in students.items():
    average = sum(grades) / len(grades)
    if average > best_average:
        best_average = average
        best_name = name
print("Найкращий:", best_name, round(best_average, 2))

# Приклад 12. Вибір структури даних
grades = [10, 8, 12]
point = (10, 20)
subjects = {"Python", "HTML", "Python"}
student = {"name": "Ivan", "grade": 11}
print(grades, point, subjects, student)