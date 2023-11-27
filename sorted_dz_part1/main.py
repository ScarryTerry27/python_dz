import random


# задание 1
def sorted_list(lst):
    end = len(lst) // 3 if sum(lst)/len(lst) <= 0 else (len(lst) // 3) * 2
    print(sum(lst)/len(lst))
    for i in range(end):
        for j in range(i):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]

    return lst[: end] + lst[end:][::-1]


lst = [random.randint(-10, 11) for i in range(21)]
print(lst)
print(sorted_list(lst))

# 2 задание


def check_ratings(ratings):
    return ratings


def retake_the_exam(ratings):
    ind, value = map(int, input('Введите номер оценки и саму оценку через пробел: ').split())
    ratings[ind] = value
    return 'Оценка исправлена'


def scholarship(ratings):
    return  'Вам назначена стипендия' if sum(ratings)/len(ratings) >= 10.7 else 'Вам отказано в стипендии'


def check_sorted_ratings(ratings):
    res = int(input('''
    введите 0, если нужно отсортировать список по неубыванию,
    введите 1, если отсортировать список по невозрастанию
    '''))
    return sorted(ratings, reverse=bool(res))


def academic_performance(ratings):
    dicti = {
        1: check_ratings,
        2: retake_the_exam,
        3: scholarship,
        4: check_sorted_ratings
        }
    res = int(input('''
    Что нужно сделать?
    1) Вывод оценок;
    2) Пересдача экзамена;
    3) Выходит ли стипендия;
    4) Вывод отсортированного списка оценок
    '''))
    return dicti[res](ratings)


ratings = [random.randint(7, 12) for i in range(20)]
print(ratings)
print(academic_performance(ratings))


# 3 задание:
def super_bubble(lst):
    flag = True
    while flag:
        print(lst)
        flag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                flag = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


lst = [random.randint(-100, 101) for _ in range(10)]
lst = super_bubble(lst)




