import math
import random
import statistics
from datetime import date

# Завдання 1. Геометричні обчислення з math
radius = float(input("Радіус: "))
katet1 = float(input("Катет 1: "))
katet2 = float(input("Катет 2: "))
items = int(input("Предметів: "))
capacity = int(input("В упаковці: "))

circle_area = math.pi * radius ** 2
hypotenuse = math.sqrt(katet1 ** 2 + katet2 ** 2)
packages_needed = math.ceil(items / capacity)

print("Площа круга:", round(circle_area, 2))
print("Гіпотенуза:", round(hypotenuse, 2))
print("Потрібно упаковок:", packages_needed)


# Завдання 2. Генератор оцінок і статистичний звіт
n = int(input("N = "))
if n > 0:
    grades = []
    for i in range(n):
        grades.append(random.randint(1, 12))
        
    print("Оцінки:", grades)
    print("Min:", min(grades))
    print("Max:", max(grades))
    print("Середнє:", round(statistics.mean(grades), 2))
    print("Медіана:", statistics.median(grades))
    
    high_count = 0
    for grade in grades:
        if grade >= 10:
            high_count += 1
    print("Оцінок 10–12:", high_count)
else:
    print("Значення N повинно бути додатним.")


# Завдання 3. Дата події
print("\n=== Завдання 3 ===")
year = int(input("Рік події: "))
month = int(input("Місяць події: "))
day = int(input("День події: "))

event_date = date(year, month, day)
today = date.today()

difference = event_date - today
days_diff = difference.days

if days_diff > 0:
    print(f"До події залишилося: {days_diff} днів")
elif days_diff < 0:
    print(f"Після події минуло: {abs(days_diff)} днів")
else:
    print("Подія відбувається сьогодні!")