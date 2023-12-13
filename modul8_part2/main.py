import random
from faker import Faker


def fake_phone_number(fake: Faker) -> str:
    return f'+7{fake.msisdn()[3:]}'


fk = Faker('ru_RU')

# z 1
dicti = {fk.name(): random.randint(189, 205) for i in range(10)}

# z 2
dictionary = {'book': 'livre', 'table': 'tableau'}

# z 3
firma = [
    {'fio': fk.name(), 'phone': fake_phone_number(fk), 'email': 'fk.email@mail.ru',
         'post': 'kto-to', 'cab_num': 1, 'skype': 'srype@@'}
    ]

# z 4
books = [
    {'author': fk.name(), 'name': 'Какое то название', 'genre': 'какойто',
         'year': random.randint(1980, 2023), 'num_page': random.randint(200, 500), 'publ': 'publishing@@'}
    ]

print(dicti, dictionary, firma, books, sep='\n')
