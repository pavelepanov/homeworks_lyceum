'''
Занятия 2.1, 2.2, 2.4 выполнил в классе
'''


def multy(x):
    return x * 3


def hello(name, lang):
    if lang == 'русский':
        return f'Привет, {name}!'
    else:
        return f'Hello, {name}!'


def series(n):
    now = 1
    now2 = 2
    mysum = 0

    while now != n:
        mysum += now * now2
        now += 1
        now2 += 1

    return mysum


def div(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count


def num_to_list(mystr, box):
    newstr = list(map(int, mystr.split()))
    box += newstr
    return box


def final_price(*prices, discount=1):
    box = []
    for i in prices:
        box.append(i * (discount/100))

    return box


def cube():
    func = (lambda x: x ** 3)(2)
    return func


def ans252():
    func = (lambda x: x[0].upper() + x[1:].lower())('неформатирОванная строкА')
    return func


def ans253():
    func = (lambda x: (int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2])) % 2 == 0)(543)
    return func


def ans254():
    a = [i for i in range(6)]
    func = (lambda x: sum(x))(a)
    return func


def ans255():
    s = 'Андрей использует Python во всех проектах'
    snew = s.split()
    func = sorted(snew, key=lambda x: (len(x), x.lower()))
    return func


def ans256():
    coords = [[3, -2], [7, 1], [0, 4]]
    new_coords = sorted(coords, key=lambda x: (x[0] ** 2 + x[1] ** 2))

    return new_coords


