from faker import Faker
from string import ascii_lowercase

fake = Faker()

with open('zadanie1_1', mode='w', encoding='utf-8') as f, open('zadanie1_2', mode='w', encoding='utf-8') as f1:
    for _ in range(10):
        print(fake.name(), file=f)
        print(fake.name(), file=f1)


# 1 задание
with open('zadanie1_1', mode='r', encoding='utf-8') as f, open('zadanie1_2', mode='r', encoding='utf-8') as f1:
    file1 = [i.strip() for i in f.readlines()]
    file2 = [i.strip() for i in f1.readlines()]
    for i in range(len(file1)):
        if file1[i] != file2[i]:
            print(file1[i], file2[i], sep='\n')


# 2 задание
with open('zadanie1_1', mode='r', encoding='utf-8') as f:
    file1 = [i.strip() for i in f.readlines()]
    count_symb = sum((len(i) for i in file1))
    count_str = len(file1)
    count_gl = sum((1 for i in file1 for l in i if l.lower() in 'eyuioa'))
    count_sgl = sum((1 for i in file1 for l in i if l.lower() in set(ascii_lowercase) - set('eyuioa')))
    count_dgt = sum((1 for i in file1 for l in i if l.lower() in '1234567890'))

# 2 задание
with open('new_file', mode='w', encoding='utf-8') as file:
    print(count_symb, count_str, count_gl, count_sgl, count_dgt, file=file)


with open('zadanie1_1', mode='r', encoding='utf-8') as f:
    file1 = [i.strip() for i in f.readlines()]


# 3 задание
with open('new_file1', mode='w', encoding='utf-8') as file:
    print('\n'.join(file1[::-1]), file=file)


# 4 задание
print(max(file1, key=lambda x: len(x)))


# 5 задание
with open('zadanie1_1', mode='r', encoding='utf-8') as f:
    file1 = f.read().lower()
    word = input()
    print(file1.count(word))


# 6 задание
    file1 = f.read().lower()
    word1 = input()
    word2 = input()
    count = file1.count(word1)
    print(file1.replace(word1, word2, count))