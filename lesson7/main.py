# # 1 задание

print(int(input())**int(input()))

# 2 задание

print(sum(1 for i in range(100, 1000) if len(set(str(i))) == 2))

# 3 задание

print(sum(1 for i in range(100, 10000) if len(set(str(i))) == len(str(i)) and not i % 2))

# 4 задание

print(''.join(list(i for i in input() if i not in ('3', '6'))))