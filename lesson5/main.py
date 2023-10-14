# 1 задание
print(*(i for i in range(int(input()), int(input()) + 1) if not i % 7))


# 2 задание
def func(a, b):
    print(*(i for i in range(a, b+1)))
    print(*list((i for i in range(a, b + 1)))[::-1])
    print(*(i for i in range(a, b + 1) if not i % 7))
    print(sum(1 for i in range(a, b + 1) if not i % 5))


print(func(int(input()), int(input())))


# 3 задание
def func2(a, b):
    for i in range(a, b+1):
        if not i % 3 and not i % 5:
            print('Fizz Buzz', end=' ')
        elif not i % 3:
            print('Fizz', end=' ')
        elif not i % 5:
            print('Buzz', end=' ')
        else:
            print(i)


func2(int(input()), int(input()))
