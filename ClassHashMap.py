from collections import defaultdict

class HaspMap:
    def __init__(self):
        self.storage = defaultdict(list)
        self.hash_func = len

    def put(self, key: str, value: int) -> None:  # O(1) в среднем
        hash_ = self.hash_func(key)
        self.storage[hash_].append((key, value))  

    def get(self,key: str) -> int | None:  # O(n), где n - глубина коллизии
        hash_ = self.hash_func(key)
        for k, v in self.storage[hash_]:
            if k == key:
                return f"Ключ: {key}, Значение: {v}"
        return None

    def storage(self):
        return self.storage
    
test = HaspMap()

test.put('Понедельник', 1)
test.put('Вторник', 2)
test.put('Четверг', 4)

print(test.get('Понедельник'))
print(test.get('Четверг'))
print(test.get('Вторник'))
print(test.get('Среда'))

print(test.storage)