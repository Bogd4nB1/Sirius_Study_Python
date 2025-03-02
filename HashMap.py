from collections import defaultdict

storage = defaultdict(list)

hash_func = len

def put(key: str, value: int) -> None:  # O(1) в среднем
    hash_ = hash_func(key)
    storage[hash_].append((key, value))  

def get(key: str) -> int | None:  # O(n), где n - глубина коллизии
    hash_ = hash_func(key)
    for k, v in storage[hash_]:
        if k == key:
            return f"Ключ: {key}, Значение: {v}"
    return None 

put('Понедельник', 1)
put('Вторник', 2)
put('Четверг', 4)

print(get('Понедельник'))
print(get('Четверг'))
print(get('Вторник'))
print(get('Среда')) 
# На примере среды можно понять прикол defaultdict
# Когда мы пытаемся достать несуществующий ключ, то он создает новый список
# по дефолту будет создан пустой массив т.к. я выбрал фабрику list 
# storage = defaultdict(list)
# из за этого не происходит ошибка KeyError и функция продолжает работу
# ну и коллизия не возникает из за фабрики list

print(storage)
