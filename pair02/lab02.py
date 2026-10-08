# Завдання 1. Числа, кратні 3 або 5
n = int(input("Введіть N: "))

sum_num = 0
count = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum_num = sum_num + i
        count = count + 1

print("Кількість:", count)
print("Сума:", sum_num)

if count > 0:
    avg = sum_num / count
    print("Середнє:", round(avg, 2))
else:
    print("Немає чисел, кратних 3 або 5")

print()

# Завдання 2. Аналіз цифр натурального числа
n = int(input("Введіть N: "))

if n == 0:
    count = 1
    sum_num = 0
    max_d = 0
    min_d = 0
else:
    temp = abs(n)
    count = 0
    sum_num = 0
    max_d = 0
    min_d = 9

    while temp > 0:
        digit = temp % 10
        count = count + 1
        sum_num = sum_num + digit
        
        if digit > max_d:
            max_d = digit
        if digit < min_d:
            min_d = digit
            
        temp = temp // 10

print("Кількість цифр:", count)
print("Сума цифр:", sum_num)
print("Найбільша цифра:", max_d)
print("Найменша цифра:", min_d)

print()

# Завдання 3. Числа, що діляться на власні цифри
n = int(input("Введіть N: "))

res = []

for i in range(1, n + 1):
    temp = i
    ok = True
    
    while temp > 0:
        digit = temp % 10
        if digit != 0:
            if i % digit != 0:
                ok = False
                break
        temp = temp // 10
        
    if ok:
        res.append(str(i))

print(" ".join(res))

print()

# Завдання 4. Рамка символами
w = int(input("Введіть ширину: "))
h = int(input("Введіть висоту: "))

if w < 3 or h < 3:
    print("Помилка: мінімальний розмір 3 x 3")
else:
    c1 = input("Введіть символ контуру: ")
    c2 = input("Введіть символ всередині: ")

    for r in range(h):
        row = ""
        for c in range(w):
            if r == 0 or r == h - 1 or c == 0 or c == w - 1:
                row = row + c1
            else:
                row = row + c2
        print(row)