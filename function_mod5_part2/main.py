# модуль 5 функции Хасаханов

from functools import reduce


def ret_pr_list(lst):
    # задание 1
    return reduce(lambda x, y: x * y, lst)


def ret_min_list(lst):
    # задание 2
    return min(lst)


def is_simple(a):
    # вспомогательная функция проверки числа на простоту
    if a == 1: return False
    for i in range(2, a):
        if not a % i:
            return False
    return True


def ret_sim_in_list(lst):
    # задание 3
    return list(filter(lambda x: x if is_simple(x) else False, lst))


def ret_del_elem_in_list(elem, lst):
    # задание 4
    return len(lst)-len([item for item in lst if item != elem])


def ret_add_list(lst1, lst2):
    # задание 5
    return lst1 + lst2


def ret_pow_list(num, lst):
    # задание 6
    return list(map(lambda x: x**num, lst))
