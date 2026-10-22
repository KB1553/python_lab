# Завдання 1. Аналіз і фільтрація списку
nums = [12, 3, 4, 14, -12, 5, 10, 16, -4]

pos = []
neg = []
even = []
mult3 = []

for x in nums:
    if x > 0:
        pos.append(x)
    if x < 0:
        neg.append(x)
    if x % 2 == 0:
        even.append(x)
    if x % 3 == 0:
        mult3.append(x)

min_val = min(nums)
max_val = max(nums)
total_sum = sum(nums)
avg_val = total_sum / len(nums)

print("Додатні:", pos)
print("Від'ємні:", neg)
print("Парні:", even)
print("Кратні 3:", mult3)
print("Min:", min_val, "; Max:", max_val, "; Sum:", total_sum, "; Average:", round(avg_val, 2))

print()

# Завдання 2. Дві групи учасників
g1 = {'Anna', 'Ivan', 'Olha'}
g2 = {'Ivan', 'Maksym', 'Olha'}

common = g1 & g2
only_g1 = g1 - g2
only_g2 = g2 - g1
all_users = g1 | g2

print("Спільні:", ", ".join(common))
print("Тільки group1:", ", ".join(only_g1))
print("Тільки group2:", ", ".join(only_g2))
print("Усі:", ", ".join(all_users))

print()

# Завдання 3. Каталог товарів
shop = {"bread": 38, "milk": 48, "cheese": 120, "tea": 75}

shop["coffee"] = 90
shop["bread"] = 40

item = "tea"
found = shop.get(item)
if found:
    print("Знайдено", item, ":", found, "грн")
else:
    print("Товар не знайдено")

min_p = 40
max_p = 100

for item, price in shop.items():
    if min_p <= price <= max_p:
        print(item, "—", price, "грн")

print()

# Завдання 4. Журнал групи
group_info = ('10-IT', '2026/2027')

journal = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}

new_name = "Olha"
new_grades = [11, 12, 10, 12, 11]

if len(new_grades) == 5 and all(1 <= g <= 12 for g in new_grades):
    journal[new_name] = new_grades

for name, grades in journal.items():
    print(name + ":", " ".join(str(g) for g in grades))

print(group_info[0], "—", group_info[1])

best_student = ""
best_avg = 0

for name, grades in journal.items():
    avg = sum(grades) / len(grades)
    print(name, "—", round(avg, 1))
    if avg > best_avg:
        best_avg = avg
        best_student = name

print("Найкращий результат:", best_student, "—", round(best_avg, 1))