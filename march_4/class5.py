# 5646
'''
Определите максимальное число в этом файле,
ограниченное двумя парами символов KK и удовлетворяющее маске «43??78???34»,
где символ ? обозначает любую цифру.
Пример такого числа: 43127812334. Найдите произведение нечётных цифр найденного числа.
229635
'''

def ans(s):
    mx = ''
    last = -1
    for i in range(len(s) - 1):
        if s[i] == 'K' and s[i + 1] == 'K':
            if last != - 1:
                s1 = s[last + 2:i]
                if len(s1) == 11 and s1.isdigit():
                    if s1[:2] == '43' and s1[4:6] == '78' and s1[9:] == '34':
                        mx = max(mx, s1)
            last = i
    m = 1
    for c in mx:
        if int(c) % 2 == 1:
            m *= int(c)
    print(m)

with open('t3.txt', 'r') as file:
    a = file.read().split()
    ans(a)
