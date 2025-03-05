# Напишите программу, на вход которой даются четыре числа a, b, c и d - каждое в своей строке. 
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] 
# на все числа отрезка [c;d]

a: int = int(input("Введите a: "))
b: int = int(input("Введите b: "))
c: int = int(input("Введите c: "))
d: int = int(input("Введите d: "))

storage: dict = {}

def multiplication(a, b, c, d):
    for i in range(a,b+1):
        for j in range(c, d+1):
            storage[f"{i}*{j}"] = i * j
    return storage

print(multiplication(a, b, c, d))
