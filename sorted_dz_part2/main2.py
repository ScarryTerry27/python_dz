import random


# задание 1
def sort_id_code(dicti):
    return [int(f'{i[0]}{i[1]}') for i in sorted(dicti, key=lambda x: x[0])]


def sort_phone_number(dicti):
    return [int(f'{i[0]}{i[1]}') for i in sorted(dicti, key=lambda x: x[1])]


def check_all(dicti):
    return [int(f'{i[0]}{i[1]}') for i in dicti]


def dictionary(lst1, lst2):
    dicti = {1: sort_id_code,
             2: sort_phone_number,
             3: check_all
             }
    new_dict = tuple(zip(lst1, lst2))
    while True:
        res = int(input('''
        Что сделать?
        1) Отсортировать по идентификационным кодам;
        2) Отсортировать по номерам телефона;
        3) Вывести список пользователей с кодами и телефонами;
        4) Выход
        '''))
        if res == 4:
            break
        print(*dicti[res](new_dict), sep='\n')


def ret_num():
    return ''.join([str(random.randint(0, 9)) for _ in range(7)])


phone_code = ['67', '87', '27', '37', '09', '65']
ls1 = [int(f"89{random.choice(phone_code)}") for _ in range(1, 11)]
ls2 = [int(f"{random.randint(1, 9)}{ret_num()}") for _ in range(10)]

dictionary(ls1, ls2)

# 2 задание


def all_books(names, years):
    new_dict = tuple(zip(names, years))
    while True:
        what = new_dict
        res = int(input('''
            Что сделать?
            1) Отсортировать по названию книг;
            2) Отсортировать по годам выпуска;
            3) Вывести список книг с названиями и годами выпуска;
            4) Выход
            '''))
        if res == 4:
            break
        elif res in (1, 2):
            what = sorted(new_dict, key=lambda x: x[res-1])

        for item in what:
            print(f'{item[0]}: {item[1]}', end='\n')

            
books = [
    'Победа', 'Поражение',
    'Строка', 'Число',
    'Голодные игры', 'Сытые игры',
    'Да', 'Нет',
    'Подозрительная сова', 'Наивный слон'
    ]
ls1 = [books[i] for i in range(10)]
ls2 = [random.randint(1970, 2023) for _ in range(10)]

all_books(ls1, ls2)