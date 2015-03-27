def bubble_sort(array):
    sorted = False
    length = len(array)
    round = 1
    while not sorted:
        sorted = True
        for i in range(0, length - round):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        round += 1
    return array

def merge_sort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = length // 2
    return merge(merge_sort(array[0:mid]), merge_sort(array[mid:length]))

def merge(list1, list2):
    merged = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    return merged + list1 + list2

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left, right, equal = [], [], [pivot]
    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])
        else:
            equal.append(array[i])
    return quick_sort(left) + equal + quick_sort(right)


print(bubble_sort([5, 4, 3, 2, 1]))
print(merge_sort([5, 4, 3, 2, 1]))
print(quick_sort([5, 4, 3, 2, 1]))
