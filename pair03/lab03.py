# Завдання 1. Статистика тексту
text = input("Введіть текст: ")

vowels = "аеєиіїоуюяaeiou"
simv_count = len(text)
lit_count = 0
dig_count = 0
space_count = 0
gol_count = 0

for char in text:
    if char.isalpha():
        lit_count += 1
        if char.lower() in vowels:
            gol_count += 1
    elif char.isdigit():
        dig_count += 1
    elif char == " ":
        space_count += 1

words = text.split()

print("Символів:", simv_count)
print("Літер:", lit_count)
print("Цифр:", dig_count)
print("Пробілів:", space_count)
print("Голосних:", gol_count)
print("Слів:", len(words))


# Завдання 2. Нормалізація ПІБ
text = input("Введіть ПІБ: ")
parts = text.split()

if len(parts) == 3:
    prizv = parts[0].capitalize()
    imja = parts[1][0].upper() + "."
    pobat = parts[2][0].upper() + "."
    print(prizv, imja + pobat)
else:
    print("Треба ввести рівно три слова (Прізвище Ім'я По-батькові)")


# Завдання 3. Анаграми
text1 = input("Перший рядок: ")
text2 = input("Другий рядок: ")

s1 = text1.lower().replace(" ", "")
s2 = text2.lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")


# Завдання 4. Аналіз речення
sentence = input("Речення: ")
words = sentence.split()

longest = words[0]
shortest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w

uniq = set()
for w in words:
    uniq.add(w.lower())

print("Найдовші:", longest)
print("Найкоротші:", shortest)
print("Унікальних слів:", len(uniq))

old_word = input("Що замінити?: ")
new_word = input("На що замінити?: ")
new_sentence = sentence.replace(old_word, new_word)
print("Після заміни:", new_sentence)