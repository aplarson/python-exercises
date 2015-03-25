from math import sqrt, floor

def factors(num):
    factors = []
    for cand in range(1, floor(sqrt(num))):
        if num % cand == 0:
            factors.append(cand)
            factors.append(num // cand)
    return factors

def bubble_sort(list, callback):
    sorted = False
    i = 0
    while not sorted:
        sorted = True
        for j in range(i + 1, len(list)):
            if callback(list[i], list[j]) == 1:
                list[i], list[j] = list[j], list[i]
                sorted = False
        i += 1
    return list

def less_than(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def greater_than(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0

def substrings(string):
    subs = []
    for i in range(0, len(string)):
        for j in range(i, len(string) + 1):
            if string[i:j] not in subs:
                subs.append(string[i:j])
    return subs

print(substrings("apple"))
