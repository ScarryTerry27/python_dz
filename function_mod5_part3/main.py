# модуль 5 функции Хасаханов
import random


def find_del(a, b):
    # задание 1
    def rec(n):
        if not a % n and not b % n:
            return n
        else:
            return rec(n-1)

    return rec(min((a, b)))


def corov(num1):
    # задание 2
    def rec(count):
        count += 1
        num2 = input()
        if str(num1) == num2:
            return count
        else:
            n1 = sum(1 for i in num2 if i in str(num1))
            n2 = sum(1 for i in range(len(num2)) if num2[i] == str(num1)[i])
            print(f'Кол-во быков: {n1}')
            print(f'Кол-во коров: {n2}')
            return rec(count)

    return rec(0)


def show_matrix(mtx):
    for m in mtx:
        for item in m:
            print(str(item).rjust(2, '0'), end=' ')
        print()


def chess(a, b):
    ''' задание 3!
    Пытался решить через рекурсию с перебором всех вариантов, однако результата ждать очень долго (цикл долго крутился),
    я воспользовался Маршрутом Яниша. Прошу простить :( '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Аргументы должны быть целыми числами')
    elif not 0 <= a < 8 or not 0 <= b < 8:
        raise ValueError('Индексы должны быть неотрицательными числами до 8')
    matrix = [
        (4, 3), (6, 2), (7, 0), (5, 1), (7, 2), (6, 0), (4, 1), (5, 3),
        (3, 2), (2, 0), (0, 1), (1, 3), (2, 5), (0, 4), (1, 6), (3, 7),
        (5, 6), (7, 7), (6, 5), (4, 4), (2, 3), (3, 1), (1, 0), (0, 2),
        (1, 4), (0, 6), (2, 7), (3, 5), (4, 7), (6, 6), (7, 4), (5, 5),
        (3, 4), (1, 5), (0, 7), (2, 6), (0, 5), (1, 7), (3, 6), (2, 4),
        (4, 5), (5, 7), (7, 6), (6, 4), (5, 2), (7, 3), (6, 1), (4, 0),
        (2, 1), (0, 0), (1, 2), (3, 3), (5, 4), (4, 6), (6, 7), (7, 5),
        (6, 3), (7, 1), (5, 0), (4, 2), (3, 0), (1, 1), (0, 3), (2, 2)
    ]
    ind = matrix.index((a, b))
    matrix, count = matrix[ind:] + matrix[:ind], 1
    mtx = [[0 for i in range(8)] for _ in range(8)]

    def rec(count):
        if matrix:
            x, y = matrix.pop(0)
            mtx[x][y] = count
            return rec(count+1)

    rec(count)
    return show_matrix(mtx)


chess(7, 1)
