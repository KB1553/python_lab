# Приклад 1. Запис одного рядка у TXT
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Привіт, Python!\n")

# Приклад 2. Режим w проти a
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Перший запуск\n")
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Новий запис\n")

# Приклад 3. with автоматично закриває файл
with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
# Тут файл уже закритий автоматично.

# Приклад 4. Читання read()
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
print("Символів:", len(text))

# Приклад 5. Порядковий перебір файлу
with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}: {line.strip()}")

# Приклад 6. strip() прибирає \n
with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)

# Приклад 7. Числа з файлу і статистика
numbers = []
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# Приклад 8. Формат «ПІБ;бал»
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(";")
        print(name, int(score))

# Приклад 9. split(';') -> поля запису
line = "Anna;Python;11"
name, subject, grade = line.split(";")
print("Учень:", name)
print("Предмет:", subject)
print("Оцінка:", int(grade))

# Приклад 10. Фільтрація записів
selected = []
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(";")
        score = int(score)
        if score > 80:
            selected.append([name, score])
print(selected)

# Приклад 11. Сортування даних у пам’яті
students = [
    ["Anna", 91],
    ["Ivan", 84],
    ["Olha", 97]
]
students.sort(key=lambda student: student[1], reverse=True)
for student in students:
    print(student[0], student[1])

# Приклад 12. Запис звіту
students = [
    ["Olha", 97],
    ["Anna", 91],
    ["Ivan", 84]
]
with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in students:
        print(f"{name};{score}", file=file)
print("Звіт result.txt створено.")