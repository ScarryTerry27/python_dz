# 1 задание
def func(a, b):
    lst = list(i for i in range(a, b+1))
    print('Четные и среднее')
    print(sum((i for i in lst if i % 2)))
    print(sum((i for i in lst if i % 2))/len(list(i for i in lst if i % 2)))
    print('Нечетные и среднее')
    print(sum((i for i in lst if not i % 2)))
    print(sum((i for i in lst if not i % 2))/len(list(i for i in lst if not i % 2)))
    print('Кратные 9ти')
    print(sum((i for i in lst if not i % 9)))
    print(sum((i for i in lst if not i % 9))/len(list(i for i in lst if not i % 9)))


func(int(input()), int(input()))

# 2 задание

print(int(input()) * input(), sep='\n')

# 3 задание

while True:
    num = int(input())
    if num == 7:
        print('Удачи')
        break
    elif num > 0:
        print('Положительное')
    elif num < 0:
        print('Отрицательное')
    elif num == 0:
        print('Равно нулю')

# 4 задание
lst = []

while True:
    num = int(input())
    if num == 7:
        print('Удачи')
        break
    lst.append(num)
    print(sum(lst), max(lst), min(lst))