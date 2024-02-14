def ans211():
    a = input()
    print(f'{a[0]}-{a[-1]}')


def ans212():
    a = input()
    print(a[2:13:2])


def ans213():
    city_1 = input().lower()
    city_2 = input().lower()
    if city_1[-1] == city_2[0]:
        print('Да')
    else:
        print('Нет')


def ans214():
    a = input()
    c = []
    for key, i in enumerate(a):
        if i == '(':
            c.append(key)
        if i == ')':
            c.append(key)

    a = a[c[0]+1:c[1]]
    print(a)


def ans215():
    text = input('Text: ')
    num = int(input('Number: '))

    if len(text) % 2 != 0:
        newtext = text + '.'
        mylen = int((num - len(newtext)) / 2)
        print(mylen)

        print(text[0] * mylen + newtext + text[-1] * mylen)
    else:
        mylen = int((num - len(text)) / 2)
        print(mylen)

        print(text[0] * mylen + text + text[-1] * mylen)


def ans216():
    glas_mass = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    else_word = ['.', ',', '?', ':', '!', ' ']
    glas = 0
    soglas = 0
    a = input('Text: ').lower()

    for i in a:
        if i in glas_mass:
            glas += 1
        if i not in glas_mass and i not in else_word:
            soglas += 1

    print(glas, soglas)


def ans221():
    print(' '.join(input().split()))


def ans222():
    a = input().split()
    b = int(input())
    print(a[b+1])


def ans223():
    print(' '.join(list(reversed(input().split()))))


def ans224():
    a = input().split()
    b = list(map(int, a))
    c = list(filter(lambda x: x < 10, b))
    print(c)


def ans225():
    num = int(input())
    my = []
    for i in range(num):
        a = input()
        if a in my:
            print(a)
        else:
            my.append(a)


def ans226():
    c = input().split()
    c = list(map(int, c))
    d = input().split()
    d = list(map(int, d))
    a = c + d
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)
