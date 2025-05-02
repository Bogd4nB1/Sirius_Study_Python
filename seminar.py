import string


def check_duplicates(duplicat):
    return len(duplicat) > len(set(duplicat))

print(check_duplicates([1,2,3, 3,3, 1]))

def palidrom_string(polindrom: str):
    final_string = ""
    start_index = 0
    end_index = -1
    for i in polindrom.lower():
        if i in string.ascii_lowercase: final_string += i
    for i in range(len(final_string) // 2):
        if final_string[start_index] == final_string[end_index]:
            start_index += 1
            end_index += -1
        else: return False
    return True
    

print(palidrom_string('anana'))

