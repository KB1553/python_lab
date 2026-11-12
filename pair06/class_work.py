# Приклад 1. math: гіпотенуза і площа круга
import math
a = 6
b = 8
hypotenuse = math.sqrt(a ** 2 + b ** 2)
radius = 5
circle_area = math.pi * radius ** 2
print("Гіпотенуза:", hypotenuse)
print("Площа круга:", round(circle_area, 2))

# Приклад 2. ceil() і floor()
import math
items = 25
capacity = 6
print("Повних упаковок:", math.floor(items / capacity))
print("Упаковок потрібно:", math.ceil(items / capacity))

# Приклад 3. random.randint(): 10 випадкових чисел
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)

# Приклад 4. random.choice(): випадковий вибір
import random
students = ["Anna", "Ivan", "Olha", "Maksym"]
selected = random.choice(students)
print("Обрано:", selected)

# Приклад 5. random.shuffle(): перемішування списку
import random
questions = [1, 2, 3, 4, 5]
random.shuffle(questions)
print("Новий порядок:", questions)

# Приклад 6. statistics.mean() і median()
import statistics
grades = [10, 8, 12, 9, 11, 10]
print("Середнє:", statistics.mean(grades))
print("Медіана:", statistics.median(grades))

# Приклад 7. Поточна дата і час
from datetime import date, datetime
print("Дата:", date.today())
print("Дата і час:", datetime.now())

# Приклад 8. Кількість днів між датами
from datetime import date
date1 = date(2026, 10, 1)
date2 = date(2026, 12, 31)
difference = date2 - date1
print("Днів:", difference.days)

# Приклад 9. Створення utils.py
# Файл utils.py
def square(number):
    return number ** 2

def is_even(number):
    return number % 2 == 0

def average(numbers):
    return sum(numbers) / len(numbers)

# Приклад 10. Імпорт власного модуля
# Файл main.py
# import utils
# numbers = [4, 8, 10, 12]
# print(utils.square(5))
# print(utils.is_even(8))
# print(utils.average(numbers))

# Приклад 11. import math та from math import sqrt
import math
print(math.sqrt(100))
from math import sqrt
print(sqrt(100))

# Приклад 12. Міні-проєкт: випадкові оцінки + статистика
import random
import statistics
grades = []
for i in range(20):
    grades.append(random.randint(1, 12))

print("Оцінки:", grades)
print("Min:", min(grades))
print("Max:", max(grades))
print("Середнє:", round(statistics.mean(grades), 2))
print("Медіана:", statistics.median(grades))
high = 0
for grade in grades:
    if grade >= 10:
        high += 1
print("Оцінок 10–12:", high)

# Приклад 13. Перше вікно Tkinter
import tkinter as tk
window = tk.Tk()
window.title("Лабораторна No6")
window.geometry("400x200")
label = tk.Label(window, text="Модулі та бібліотеки Python")
label.pack(pady=20)
button = tk.Button(window, text="Закрити", command=window.destroy)
button.pack(pady=10)
window.mainloop()

# Приклад 14. Поле введення та кнопка
import tkinter as tk
def greet():
    name = name_entry.get().strip()
    if name == "":
        result.configure(text="Введіть ім’я")
    else:
        result.configure(text="Вітаю, " + name + "!")

window = tk.Tk()
window.title("Привітання")
window.geometry("400x250")
tk.Label(window, text="Ваше ім’я:").pack(pady=5)
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)
tk.Button(window, text="Привітатися", command=greet).pack(pady=10)
result = tk.Label(window, text="")
result.pack(pady=5)
window.mainloop()

# Приклад 15. Tkinter разом із random та statistics
import tkinter as tk
import random
import statistics
def generate_report():
    value = count_entry.get().strip()
    if not value.isdecimal():
        result.configure(text="Введіть ціле число від 1 до 100")
        return
    count = int(value)
    if count < 1 or count > 100:
        result.configure(text="Кількість має бути від 1 до 100")
        return
    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
    average = statistics.mean(grades)
    median = statistics.median(grades)
    text = "Оцінки: " + str(grades)
    text += "\nСереднє: " + str(round(average, 2))
    text += "\nМедіана: " + str(median)
    result.configure(text=text)

window = tk.Tk()
window.title("Генератор оцінок")
window.geometry("500x350")
tk.Label(window, text="Кількість оцінок (1–100):").pack(pady=5)
count_entry = tk.Entry(window)
count_entry.pack(pady=5)
tk.Button(window, text="Згенерувати", command=generate_report).pack(pady=10)
result = tk.Label(window, text="", wraplength=460, justify="left")
result.pack(pady=10)
window.mainloop()