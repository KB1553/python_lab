import tkinter as tk
import student_utils

def generate_report():
    value = count_entry.get().strip()

    if not value.isdecimal():
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Помилка: введіть ціле число від 1 до 20!")
        return
        
    count = int(value)
    if count < 1 or count > 20:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Помилка: кількість має бути від 1 до 20!")
        return
        
    students = ["Anna", "Ivan", "Olha"]
    report = ""
    
    print("--- Звіт у консолі ---")
    for name in students:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        
        line = f"{name}: {grades} -> {round(avg, 1)} -> {level}\n"
        report += line
        print(line.strip())
        
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, report)

window = tk.Tk()
window.title("Статистика учнів")
window.geometry("500x400")

tk.Label(window, text="Кількість оцінок (1–20):").pack(pady=5)
count_entry = tk.Entry(window, width=20)
count_entry.pack(pady=5)

tk.Button(window, text="Сформувати звіт", command=generate_report).pack(pady=10)

result_text = tk.Text(window, width=55, height=14, wrap="word")
result_text.pack(pady=5)

window.mainloop()