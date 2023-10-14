# 1 задание
def check_count(num):
    count = -2
    for i in range(1, num+1):
        if not num % i:
            count += 1
            if i != num and count == 2:
                count += 1
        if count > 2:
            break
    return count


print(*(i for i in range(int(input()), int(input())) if not check_count(i)))


# 2 Задание
def create_table(num):
    # данная функция для второго и третьего задания
    print(*(f'{num} * {i} = {i*num}'.ljust(13) for i in range(1, 11)))


for i in range(1, 11):
    create_table(i)

# 3 задание
for i in range(int(input()), int(input())+1):
    create_table(i)