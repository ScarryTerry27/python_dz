from random import randint


def partition(array: list, left: int, right: int) -> int:
    rand = randint(left, right)
    array[rand], array[left] = array[left], array[rand]
    x = array[left]
    j = left
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]

    array[left], array[j] = array[j], array[left]

    return j


def quick_sort(array: list, left: int, right: int) -> None:
    if left < right:
        m = partition(array, left, right)
        quick_sort(array, left, m - 1)
        quick_sort(array, m + 1, right)


a = [6, 1, 4, 12, 13, 10, 7, 8]
print(quick_sort(a, 0, len(a)-1))
print(a)