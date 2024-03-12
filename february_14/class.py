# 12 28 13 29

def ans_28():
    a = list(map(int, input().split()))
    my_min = 999999999999999999999999999
    my_max = 0
    mink = 0
    maxk = 0
    for key, value in enumerate(a):
        if value < my_min:
            my_min = value
            mink = key
        if value > my_max:
            my_max = value
            maxk = key

    minc = a.index(my_min)
    maxc = a.index(my_max)

    if mink < maxk:
        d = a[:minc+1] + a[maxc:]
    else:
        d = a[:maxc+1] + a[minc:]
    print(d)


def ans_13():
    n = input('колво выстрелов ')
    answer = []
    a = []
    for i in range(int(n)):
        a.append(int(input('0 или 1 ')))
    zero = 1
    one = 0
    for i in a:
        if i == 0:
            zero += 1
            answer.append(one/zero*100)
        if i == 1:
            one += 1
            answer.append(one / zero * 100)
    print(answer)


def ans_29():
    a = list(map(int, input().split()))
    sred = sum(a)/len(a)
    for key, value in enumerate(a):
        if value > sred:
            a.pop(key)

    print(a)


def ans_12():
    a = list(map(int, input().split()))
    minc = 9999999999999999999999
    for key, value in enumerate(a):
        if value < minc:
            minc = value
            mink = key

    a.pop(mink)

    minc = 9999999999999999999999
    for key, value in enumerate(a):
        if value < minc:
            minc = value

    print(minc)
