'''
Реализуйте генератор fibonacci(n), который будет выдавать n чисел из последовательности Фибоначчи.
'''
def fibonacci(nums):
    first_num, second_num = 0, 1 
    for _ in range(nums):
        yield first_num
        first_num, second_num = second_num, first_num + second_num


for i in fibonacci(5):
    print(i)