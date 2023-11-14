# модуль 5 функции Хасаханов

def func(string):
    return len(set(filter(lambda x: x.lower() if string.lower().count(x) > 1 else False, string.lower())))

