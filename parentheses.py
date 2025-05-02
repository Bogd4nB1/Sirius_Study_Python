def parentheses(seq: str):
    storage = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in seq:
        if i in storage:
            stack.append(i)
        else:
            if not stack:
                return False
            j = stack.pop()
            if storage[j] != i:
                return False
    if stack:
        return False
    return True

print(parentheses('[({})]'))

