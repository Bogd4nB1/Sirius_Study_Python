def biology(symbols: str):
    storage: dict = {}
    itog_string = ""
    for i in symbols:
        if i not in storage:
            storage[i] = 0
        storage[i] += 1
    for key, value in storage.items():
        itog_string += f"{key}{value}"
    return itog_string

print(biology("aaaabbc"))