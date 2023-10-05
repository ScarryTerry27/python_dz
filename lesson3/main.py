# 1 задание
from datetime import date

weekdays = {1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье'}
day = int(input())
if day in range(1, 8):
    print(weekdays[day])
else:
    print('Ошибка')

# 2 задание

months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
            8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

month = int(input())
if month in range(1, 13):
    print(months[month])
else:
    print('Ошибка')

# 3 задание

num = int(input())
if not num:
    print('Number is equal to zero')
elif num > 0:
    print('Number is positive')
else:
    print('Number is negative')

# 4 задание

a, b = int(input()), int(input())
if not a == b:
    print(*sorted((a, b)), sep='\n')
