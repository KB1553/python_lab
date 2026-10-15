# Приклад 1. Перший і останній символ
text = input("Введіть слово: ")
print("Перший:", text[0])
print("Останній:", text[-1])

# Приклад 2. Зрізи рядка
text = "Programming"
print(text[:7])
print(text[3:8])
print(text[::2])

# Приклад 3. Розворот рядка
text = input("Текст: ")
print(text[::-1])

# Приклад 4. Підрахунок голосних, цифр і пробілів
text = input("Введіть текст: ")
vowels = "аеєиіїоуюяaeiou"
vowel_count = 0
digit_count = 0
space_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    if char.isdigit():
        digit_count += 1
    if char == " ":
        space_count += 1

print("Голосних:", vowel_count)
print("Цифр:", digit_count)
print("Пробілів:", space_count)

# Приклад 5. Перевірка паліндрома після нормалізації
text = input("Текст: ")
normalized = text.lower().replace(" ", "")
if normalized == normalized[::-1]:
    print("Паліндром")
else:
    print("Не паліндром")

# Приклад 6. split() та join()
sentence = input("Речення: ")
words = sentence.split()
print(words)
print("-".join(words))

# Приклад 7. Пошук найдовшого слова
sentence = input("Речення: ")
words = sentence.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Найдовше слово:", longest)

# Приклад 8. replace() та очищення тексту
text = " Python, Python, Python! "
text = text.strip()
text = text.replace("Python", "JavaScript")
print(text)

# Приклад 9. Перевірка простого ідентифікатора
code = input("Код: ")
if code.isalnum() and code[0].isalpha():
    print("Формат коректний")
else:
    print("Некоректний формат")

# Приклад 10. Анаграми
text1 = input("Перший рядок: ")
text2 = input("Другий рядок: ")

a = text1.lower().replace(" ", "")
b = text2.lower().replace(" ", "")

if sorted(a) == sorted(b):
    print("Анаграми")
else:
    print("Не анаграми")

# Приклад 11. Простий зсув символів
text = input("Текст: ")
result = ""

for char in text:
    result += chr(ord(char) + 1)

print("Результат:", result)