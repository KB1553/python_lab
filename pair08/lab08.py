# Завдання 1. Безпечний калькулятор
print("Завдання 1 ----------------------")
try:
    a = float(input("A: "))
    b = float(input("B: "))
    op = input("Операція (+, -, *, /): ").strip()

    if op not in ["+", "-", "*", "/"]:
        raise ValueError("невідома операція.")

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("на нуль ділити не можна.")
        res = a / b

    print("Результат:", res)
except ValueError as err:
    if str(err) == "невідома операція.":
        print("Помилка: невідома операція.")
    else:
        print("Помилка: введіть коректні числа.")
except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна.")


# Завдання 2. Надійне введення оцінки
print("Завдання 2 ----------------------")
def input_grade():
    while True:
        try:
            grade = int(input("Оцінка: "))
            if grade < 1 or grade > 12:
                raise ValueError("оцінка повинна бути від 1 до 12.")
            return grade
        except ValueError as err:
            if "оцінка повинна бути" in str(err):
                print("Помилка: оцінка повинна бути від 1 до 12.")
            else:
                print("Помилка: потрібно ввести ціле число.")

grade = input_grade()
print("Прийнято:", grade)


# Завдання 3. Безпечний пошук у колекціях
print("Завдання 3 ----------------------")
students = ["Anna", "Ivan", "Olha", "Maksym"]
subjects = {
    "math": 11,
    "python": 12,
    "history": 10
}

choice = input("1 - учень, 2 - предмет: ").strip()

if choice == "1":
    try:
        idx = int(input("Індекс: "))
        print("Учень:", students[idx])
    except ValueError:
        print("Помилка: індекс повинен бути цілим числом.")
    except IndexError:
        print("Помилка: учня з таким індексом немає.")
elif choice == "2":
    subj = input("Предмет: ").strip().lower()
    try:
        print("Оцінка:", subjects[subj])
    except KeyError:
        print("Помилка: такого предмета немає у словнику.")
else:
    print("Помилка: невідомий пункт меню. Оберіть 1 або 2.")


# Завдання 4. Надійна обробка файлу студентів
print("Завдання 4 ----------------------")
valid_records = []
skipped_count = 0

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for line_num, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line:
                continue

            parts = line.split(";")
            if len(parts) != 2:
                print(f"Рядок {line_num} пропущено: неправильний формат запису (очікується ПІБ;Бал).")
                skipped_count += 1
                continue

            name = parts[0].strip()
            score_str = parts[1].strip()

            if not name:
                print(f"Рядок {line_num} пропущено: порожнє ім'я учня.")
                skipped_count += 1
                continue

            try:
                score = int(score_str)
            except ValueError:
                print(f"Рядок {line_num} пропущено: бал не є числом.")
                skipped_count += 1
                continue

            if score < 0 or score > 100:
                print(f"Рядок {line_num} пропущено: бал поза діапазоном.")
                skipped_count += 1
                continue

            valid_records.append([name, score])

    valid_records.sort(key=lambda item: item[1], reverse=True)

    with open("report.txt", "w", encoding="utf-8") as out:
        for name, score in valid_records:
            out.write(f"{name};{score}\n")

    print(f"Правильних записів: {len(valid_records)}")
    print(f"Пропущено: {skipped_count}")
    print("Створено report.txt")

except FileNotFoundError:
    print("Помилка: файл students.txt не знайдено.")