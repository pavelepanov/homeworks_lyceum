# № 6286
'''
Текст разбит на строки различной длины.
Для каждой строки нужно определить букву (или буквы), которая встречается в этой строке чаще всего после буквы X.
Все эти буквы добавляются в новый список.
Найдите букву, которая чаще всего встречается в построенном списке, и в качестве ответа укажите, сколько раз она там встретилась.
928
'''

def ans(f):
    r = [0] * 26;
    for s in f:
        s = s.strip()
        k = [0] * 26
        for i in range(1, len(s)):
            if s[i-1] == 'X':
                k[ord(s[i]) - 65] += 1
        mx = max(k)
        for i in range(26):
            if k[i] == mx:
                r[i] += 1
    print(max(r))

with open('t2.txt', 'r') as file:
    a = file.read().split()
    ans(a)