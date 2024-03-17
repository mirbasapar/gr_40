def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(item, arr):
    result_ok = False
    first = 0
    last = len(arr) - 1
    pos = None

    while first <= last:
        middle = (first + last) // 2
        if item == arr[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
            break
        elif item > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f'Item found: the item "{item}" is in position {pos}')
    else:
        print(f'Item not found')
    return result_ok


list = [5, 3, 6, 2, 10, 8, 12, 7]
print(f'Sorted list: {bubble_sort(list)}')
binary_search(10, bubble_sort(list))
