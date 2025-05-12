'''
Напишите класс FlattenIterator, который принимает вложенный список (любой глубины)
и итеративно возвращает все элементы в плоском виде.

(!) Решение не должно использовать рекурсию в next, а работать итеративно
'''
class FlattenIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list  # Сохраняем исходный список
    
    def __iter__(self):
        # Создаем новый стек при каждом вызове __iter__
        self.stack = [iter(self.nested_list)]
        return self
    
    def __next__(self):
        while self.stack:
            try:
                element = next(self.stack[-1])
                if isinstance(element, list):
                    self.stack.append(iter(element))
                else:
                    return element
            except StopIteration:
                self.stack.pop()
        
        raise StopIteration

# Тестирование
nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)