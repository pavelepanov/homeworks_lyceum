from functools import reduce


def factorial(x):
    fac = 1
    while x > 1:
        fac = fac * x
        x = x - 1
    return fac


def simples(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def simples_n(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes


func = lambda n: reduce(lambda x, y: x * y, [i for i in range(1, n+1)], 1)


USERS = {
    "admin": "admin",
    "Doberman": "derparol",
    "BabValya": "12345",
}


def check_pass(name, password):
    if name in USERS:
        if USERS[name] == password:
            return True
        else:
            print("НЕВЕРНЫЙ ПАРОЛЬ!")
            return False
    else:
        print("ПОЛЬЗОВАТЕЛЬ НЕ ОБНАРУЖЕН!")
        return False


def authorize():
    while True:
        a = input().split()
        if len(a) > 2:
            print("ОШИБКА АВТОРИЗАЦИИ!")
        if check_pass(a[0], a[1]):
            print("УСПЕШНО" )
            return True