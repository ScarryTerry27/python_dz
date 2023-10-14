def create_pic1():
    print(*(f"{'*'*i}".rjust(7) for i in range(7, 0, -1)), sep='\n')


def create_pic2():
    print(*(f"{'*'*i}".ljust(7) for i in range(1, 8)), sep='\n')


def create_pic3():
    print(*(f"{' '* int((7-i)/2)}{'*'*i}" for i in range(7, 0, -2)), sep='\n')


def create_pic4():
    print(*(f"{' '* int((7-i)/2)}{'*'*i}" for i in range(1, 8, 2)), sep='\n')


def create_pic5():
    create_pic3()
    create_pic4()


def create_pic6():
    print(*(f"{'*' * i}{' ' * (7-(i*2))}{'*' * i}" for i in range(1, 4)), sep='\n')
    print('*' * 7)
    print(*(f"{'*' * i}{' ' * (7 - (i * 2))}{'*' * i}" for i in range(3, 0, -1)), sep='\n')


def create_pic7():
    print(*(f"{'*'* i}" for i in range(1, 5)), sep='\n')
    print(*(f"{'*' * i}" for i in range(3, 0, -1)), sep='\n')


def create_pic8():
    print(*(f"{'*'* i}".rjust(7) for i in range(1, 5)), sep='\n')
    print(*(f"{'*' * i}".rjust(7) for i in range(3, 0, -1)), sep='\n')


def create_pic9():
    print(*(f"{'*' * i}" for i in range(7, 0, -1)), sep='\n')


def create_pic10():
    print(*(f"{'*' * i}".rjust(7) for i in range(1, 8)), sep='\n')


dicti = {
    1: create_pic1,
    2: create_pic2,
    3: create_pic3,
    4: create_pic4,
    5: create_pic5,
    6: create_pic6,
    7: create_pic7,
    8: create_pic8,
    9: create_pic9,
    10: create_pic10
    }

pic = int(input('Ввведите число от 1 до 10 в зависимости от того, какую фигуру вывести\n'))
dicti[pic]()
