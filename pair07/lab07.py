# Завдання 1. Аналіз текстового файлу
print("Завдання 1 --------------------------------")
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()

max_num = 0
max_len = -1
max_line = ""

for num, line in enumerate(lines, start=1):
    if len(line) > max_len:
        max_len = len(line)
        max_num = num
        max_line = line

print(f"Рядків: {len(lines)}")
print(f"Слів: {len(words)}")
print(f"Символів: {len(text)}")
print(f"Найдовший рядок: №{max_num}, {max_len} символів")
print(f"Текст: {max_line}")


# Завдання 2. Пошук фрагмента у файлі
print("Завдання 2 --------------------------------")
search = input("Введіть фрагмент для пошуку: ").strip().lower()
found = []

with open("text.txt", "r", encoding="utf-8") as f:
    for num, line in enumerate(f, start=1):
        clean = line.rstrip("\r\n")
        if search in clean.lower():
            found.append((num, clean))

if found:
    for num, clean in found:
        print(f"{num}: {clean}")
else:
    print("Збігів не знайдено.")


# Завдання 3. Результати студентів
print("Завдання 3 --------------------------------")
best_list = []

with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, score_text = line.split(";")
        score = int(score_text)
        if score > 80:
            best_list.append([name, score])

best_list.sort(key=lambda x: x[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as out:
    for name, score in best_list:
        out.write(f"{name};{score}\n")

print("Файл result.txt сформовано.")


# Завдання 4. CSV-подібний журнал оцінок
print("Завдання 4 --------------------------------")

def get_grades(filename):
    data = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, subject, grade_text = line.split(";")
            grade = int(grade_text)
            if name not in data:
                data[name] = []
            data[name].append(grade)
    return data

def count_stats(data):
    result = []
    for name, grades in data.items():
        avg = sum(grades) / len(grades)
        result.append([name, len(grades), avg])
    result.sort(key=lambda x: x[2], reverse=True)
    return result

def find_top(result):
    if not result:
        return [], 0.0
    top_avg = result[0][2]
    top_names = [row[0] for row in result if abs(row[2] - top_avg) < 1e-9]
    return top_names, top_avg

def make_report(result, top_names, top_avg):
    lines = []
    for name, count, avg in result:
        lines.append(f"{name} — оцінок: {count} — середній: {avg:.2f}")
    lines.append("Найкращий результат:")
    lines.append(f"{' та '.join(top_names)} — {top_avg:.2f}")
    return "\n".join(lines) + "\n"

grades_data = get_grades("grades.csv")
stats = count_stats(grades_data)
top_students, best_score = find_top(stats)
report = make_report(stats, top_students, best_score)

with open("report.txt", "w", encoding="utf-8") as out:
    out.write(report)

print(report.strip())