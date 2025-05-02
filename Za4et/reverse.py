'''
Дана строка s и целое число k, поменяйте местами первые k символов каждые 2k символов, 
считая от начала строки.
Если количество символов меньше 2k, но больше или равно k, 
то поменяйте местами первые k символов, а остальные оставьте исходными.
'''

def reverseStr(s, k):
    s = list(s)
    for i in range(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k]) # reversed() возвращает итератор, поэтому лучше чем s[::-1]
    return ''.join(s)

print(reverseStr("abcdefg", 2))
print(reverseStr("abcd", 2))
print(reverseStr("a", 1))