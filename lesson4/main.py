# задание 1
def check_num(num):
    res = num
    if not num % 3 and not num % 5:
        res = 'Fizz Buzz'
    elif not num % 3:
        res = 'Fizz'
    elif not num % 5:
        res = 'Buzz'
    return res


number = int(input())
if 0 < number < 101:
    print(check_num(number))
else:
    print('ошибка')

# задание 2
num = int(input())
print(*list(pow(num, i) for i in range(1, 8)), sep='\n')

# задание 3

operators = {
    'Mts': [1.1, 0.5],
    'Beline': [0.9, 0.3],
    'Megafon': [0.7, 0.2]
}
# первая цена на внешние звонки, вторая внутри одного оператора

time = int(input('Введите время разговора '))
op1 = input('Введите вашего оператора в латинице ')
op2 = input('Введите оператора собеседника в латинице ')

if not all((op1.capitalize() in operators.keys(), op2.capitalize() not in operators.keys())):
    print('Нет данных по данным операторам')
elif op1.lower() == op2.lower():
    print(operators[op1.capitalize()][1]*time)
else:
    print(operators[op1.capitalize()][0] * time)

# задание 4

dicti = ((1000, 0.08), (500, 0.05), (0, 0.03))

managers = {input('введите имя продавца '): [int(input('Введите общую сумму проданных товаров '))] for _ in range(3)}
for key, value in managers.items():
    for i in dicti:
        if value[0] > i[0]:
            value.append(200+value[0]*i[1])
            break

the_best = max(managers, key=lambda x: managers[x][1])
managers[the_best][1] += 200
print(f' Лучший продавец: {the_best}\nЕго зарплата: {managers[the_best][1]}')
print(managers)
