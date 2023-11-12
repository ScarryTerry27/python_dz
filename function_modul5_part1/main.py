# модуль 5 функции Хасаханов
from functools import reduce


def print_text():
    # задание 1
    print('''“Don't compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                            Bill Gates''')


def check_even_in_interval(a, b):
    # задание 2
    print(*(i for i in range(a, b+1) if i % 2))


def draw_square(length, symbol, fill=True):
    # задание 3
    if fill:
        matrix = [[symbol for _ in range(length)] for _ in range(length)]
    else:
        matrix = [[
            symbol if any((j in (0, length-1), i in (0, length-1))) else ' ' for j in range(length)] for i in range(length)
        ]
    for m in matrix:
        print(*m)


def return_min(*args):
    # задание 4
    if len(args) > 5:
        return 'Должно быть 5 элементов по условию заданий'
    return min(args)


def return_pr(a, b):
    # задание 5
    if a > b:
        a, b = b, a
    return reduce(lambda x, y: x * y, (range(a, b+1)))


# задание 6
length_num = lambda x: len(str(x))

# задание 7
num_is_pal = lambda x: str(x) == str(x)[::-1]






