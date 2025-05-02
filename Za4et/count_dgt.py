'''
Напишите программу, которая считает, сколько раз каждая цифра встречается в числе. 
Гарантируется, что на вход подаются только положительные целые числа, не выходящие за диапазон int.
'''
from collections import defaultdict, Counter

# 1 реализация задачи с defaultdict
def count_dgt_v1():
    number = input("Введите число: ")
    digit_counts = defaultdict(int)

    for digit in number:
        digit_counts[digit] += 1

    for digit in sorted(digit_counts):
        print(f"{digit}: {digit_counts[digit]}")

# 2 реализация задачи с Counter (мне эта нравится больше, но это готовый модуль не знаю можно ли его использовать)
def count_dgt_v2():
    number = str(input("Введите число: "))
    digit_counts = Counter(number)

    print(digit_counts)  # Вывод: Counter({'0': 4, '1': 1, '5': 1})

# 3 реализация без коллекций
def count_dgt_v3():
    number = input("Введите число: ")
    digit_counts = {}

    for dgt in number:
        if dgt in digit_counts:
            digit_counts[dgt] += 1
        else:
            digit_counts[dgt] = 1
    
    for key, value in sorted(digit_counts.items()):
        print(f"{key}: {value}")

count_dgt_v1()
count_dgt_v2()
count_dgt_v3()