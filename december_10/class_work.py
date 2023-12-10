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


def list_to_list(vesh: list[float]):
    new = list(map(str, vesh))
    return new


def reverse_list(mystr: list[str]):
    func = list(map(lambda x: x[::-1] + '!', mystr))
    return func


def for_complex(x):
    if x % 2 == 0 and x % 4 == 0:
        return x


def complex_filter(box: list[int]):
    new = list(filter(for_complex, box))
    return new


def filter_unique_words(text):
    word = text.split()
    new = list(filter(lambda x: word.count(x) == 1, word))
    return new


def compare_test_results(box1, box2, names):
    def check_score(score):
        return "Да" if score >= 60 else "Нет"

    results = list(zip(box1, box2))
    final_results = list(map(lambda x: ( check_score(x[0]), check_score(x[1])), results))
    final_results = list(zip(names, final_results))
    return final_results


def long_livers(box1, box2):
    def longs(age):
        return age >= 90

    long_livers = list(filter(lambda x: longs(x[0]), zip(box1, box2)))
    return long_livers
