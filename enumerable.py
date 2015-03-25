def double_nums(list):
    result = []
    for el in list:
        result.append(el * 2)
    return result

def my_each(list, callback):
    for el in list:
        callback(el)
    return list

def median(list):
    length = len(list)
    if length % 2 == 0:
        return (list[length // 2] + list[(length // 2) - 1]) / 2
    else:
        return list[length // 2]

def mass_concat(strings):
    result = ""
    for string in strings:
        result += string
    return result

print(median([1, 2, 3]))
print(median([1, 2, 3, 4]))
print(mass_concat(["Hello ", "there ", "world ", "how ", "are ", "you"]))
