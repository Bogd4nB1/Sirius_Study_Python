'''
Напишите класс FlattenIterator, который принимает вложенный список (любой глубины)
и итеративно возвращает все элементы в плоском виде.

(!) Решение не должно использовать рекурсию в next, а работать итеративно
'''
class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = []
        self.stack.append(iter(nested_list))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.stack:
            try:
                # Берем элемент из текущего итератора на вершине стека
                element = next(self.stack[-1])
                if isinstance(element, list):
                    self.stack.append(iter(element))
                else:
                    return element
            except StopIteration:
                self.stack.pop()
        
        raise StopIteration

nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)