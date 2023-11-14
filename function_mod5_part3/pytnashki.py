import random
''' Данную игру запускать в пайтон консоли
Чтобы начать игру, создайте экземпляр класса Pole, например
"pole = Pole()"
Чтобы сделать ход, запишите команду, по типу
<имя экземпляра класса>.pole(<ячейка, которую двинуть>)
например 
pole.step(7)'''

class Cell:
    def __init__(self, name, step = False):
        self.name = name
        self.step = False

    def check_value(self, val):
        if not isinstance(val, int):
            raise TypeError('Аргумент должен быть положительным числом')
        elif not 0 <= val < 4:
            raise ValueError('Аргумент должен быть положительным числом от 0 до 3х включительно')


class Pole:
    def __init__(self):
        self.create_pole()
        self.count = 0
        self.show()

    def create_pole(self):
        mtx = list(range(1, 16)) + [0]
        self.pole = []
        for line in range(4):
            l = []
            for item in range(4):
                x = random.choice(mtx)
                mtx.pop(mtx.index(x))
                l.append((Cell(str(x))))
                if x == 0:
                    self.cell_empty = (line, item)

            self.pole.append(l)
        self.add_step(self.cell_empty)

    def add_step(self, indx):
        x, y = indx
        for line in self.pole:
            for item in line:
                item.step = False

        for dx, dy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= dx < 4 and 0 <= dy < 4:
                self.pole[dx][dy].step = True

    def show(self):
        for line in self.pole:
            for item in line:
                print(item.name.rjust(2, '0'), end=' ')
            print()

    def step(self, name):
        for line in range(len(self.pole)):
            for item in range(len(self.pole[line])):
                if self.pole[line][item].name == str(name):
                    x, y = line, item
                    break

        if self.pole[x][y].step:
            self.pole[self.cell_empty[0]][self.cell_empty[1]], self.pole[x][y] = self.pole[x][y], self.pole[self.cell_empty[0]][self.cell_empty[1]]
            self.cell_empty = (x, y)
            self.add_step((self.cell_empty))
        else:
            print('Эта ячейка не может ходить')

        self.count += 1
        if self.check_win():
            print(f'Вы выиграли! Вы потратили для этого {self.count} ходов')
        else:
            print(f'Вы сделали {self.count} ходов')

        self.show()

    def check_win(self):
        mtx = list(range(1, 16)) + [0]
        c = 0
        flag = True
        for line in self.pole:
            for item in line:
                if not item.name == str(mtx[c]):
                    flag = False
                    break
                c += 1
        return flag


