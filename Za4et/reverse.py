'''
Дана строка s и целое число k, поменяйте местами первые k символов каждые 2k символов, 
считая от начала строки.
Если количество символов меньше 2k, но больше или равно k, 
то поменяйте местами первые k символов, а остальные оставьте исходными.
'''

def reverseStr(input_string, chunk_size):
    chars = list(input_string)
    for i in range(0, len(chars), 2 * chunk_size):
        # Переворачиваем первые k символов каждого 2k блока
        chars[i:i + chunk_size] = reversed(chars[i:i + chunk_size])
    return ''.join(chars)

print(reverseStr("abcdefg", 2))
print(reverseStr("abcd", 2))
print(reverseStr("a", 1))