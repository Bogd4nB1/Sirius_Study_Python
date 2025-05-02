def biology(symbols: str):
    storage: dict = {}
    itog_string = ""
    for i in symbols:
        if i not in storage:
            storage[i] = 1
        if i == storage[i]:
            storage[i] += 1
        print(storage)
    
    return storage
print(biology("aaaabbсaa"))