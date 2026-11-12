import random
import statistics

def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
    return grades

def average_grade(grades):
    if not grades:
        return 0.0
    return statistics.mean(grades)

def get_level(avg):
    if avg >= 10:
        return "високий"
    elif avg >= 7:
        return "достатній"
    elif avg >= 4:
        return "середній"
    else:
        return "початковий"