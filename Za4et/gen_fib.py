'''
Реализуйте генератор fibonacci(n), который будет выдавать n чисел из последовательности Фибоначчи.
'''
def fibonacci(n):
    a, b = 0, 1 
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(20):
    print(i)