# № 6286
'''
Текст разбит на строки различной длины.
Для каждой строки нужно определить букву (или буквы), которая встречается в этой строке чаще всего после буквы X.
Все эти буквы добавляются в новый список.
Найдите букву, которая чаще всего встречается в построенном списке, и в качестве ответа укажите, сколько раз она там встретилась.
928
'''
from collections import Counter

def ans(mytxt):
    c = dict()
    full = dict()
    m = []
    n = 0
    for i in mytxt:
        a = set(i)
        for j in a:
            c[j] = i.count(j)
        for key, value in c.items():
            if value > n:
                n = value
                m.append(key)
        n = 0
    my = Counter(m)
    l = 0
    for key, value in my.items():
        if value >= l:
            l = value
    print(l)

with open('t2.txt', 'r') as file:
    a = file.read().split()
    ans(a)
