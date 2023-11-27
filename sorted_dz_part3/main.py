import random


def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)
    i, j = 0, 0

    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def split_and_merge_list(lst):
    mid = len(lst)//2
    lst1 = lst[:mid]
    lst2 = lst[mid:]
    if len(lst1) > 1:
        lst1 = split_and_merge_list(lst1)
    if len(lst2) > 1:
        lst2 = split_and_merge_list(lst2)

    return merge_list(lst1, lst2)


# задание 1
def user_choice():
    a = merge_list(split_and_merge_list(ls1), split_and_merge_list(ls2))
    b = merge_list(split_and_merge_list(ls3), split_and_merge_list(ls4))
    res = int(input('''
    Что сделать
    1) Отсортировать по возрастанию
    2) Отсортировать по убыванию
    '''))
    res2 = int(input('''
    Введите число, которое нужно найти
    '''))
    ret_list = merge_list(a, b) if not res-1 else merge_list(a, b)[::-1]
    for item in enumerate(ret_list):
        if item [1] == res2:
            print(f'Индекс элемента {item[0]}')
            break
    else:
        print('Элемент не найден')

    return ret_list


ls1, ls2, ls3, ls4 = ([random.randint(-100, 100) for _ in range(10)] for _ in range(4))

print(user_choice())

# задание 2


def find_binar(list_find, item):
    elem = len(list_find)//2
    if len(list_find) == 1 and item != list_find[0][1]:
        return 'Элемент не найден'
    if item < list_find[elem][1]:
        return find_binar(list_find[:elem], item)
    elif item > list_find[elem][1]:
        return find_binar(list_find[elem+1:], item)
    else:
        return f'Элемент найден по индексу {list_find[elem][0]}'


def user_choice1():
    a = merge_list(split_and_merge_list(list(x1)), split_and_merge_list(list(x2)))
    b = merge_list(split_and_merge_list(list(x3)), split_and_merge_list(list(x4)))
    res = int(input('''
    Что сделать
    1) Отсортировать по возрастанию
    2) Отсортировать по убыванию
    '''))
    res2 = int(input('''
    Введите число, которое нужно найти
    '''))
    ret_list = merge_list(a, b) if not res - 1 else merge_list(a, b)[::-1]
    print(find_binar(list(enumerate(ret_list)), res2))

    return ret_list


x1, x2, x3, x4 = (set([random.randint(-10, 10) for _ in range(10)]) for _ in range(4))
print(user_choice1())