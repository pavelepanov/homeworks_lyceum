# 5646
'''
Определите максимальное число в этом файле, ограниченное двумя парами символов KK и удовлетворяющее маске «43??78???34»,
где символ ? обозначает любую цифру.
229635
'''
def ans(mytxt):
    mymax = 0
    k = 0
    l = []
    for i in mytxt:
        if len(l) < 2:
            if i == 'K':
                l.append(1)
            k += 1
        else:
            if k > mymax:
                mymax = k
            l.clear()
            k = 0

    print(mymax)



with open('t3.txt', 'r') as file:
    a = file.read().split()
    ans(a)
