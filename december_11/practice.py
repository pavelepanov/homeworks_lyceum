from math import sqrt


def ans9(n: int, x: float):
    '''
    n - степень
    x - само число
    '''

    def chisl(x: float, n: int):
        return (x* (n**x - 1))

    def znam(x: float, n: int):
        return (x - (2**n))

    some_n = 1
    f = 1

    while some_n != n:
        a1 = ((chisl(x=x, n=some_n))/(znam(x=x, n=some_n)))
        a2 = ((chisl(x=x, n=some_n+1))/(znam(x=x, n=some_n+1)))
        f = a1 * a2
        some_n += 1

    return f


def ans12(k: int, n: int):

    mysum = 0
    some_n = 1

    def some_sqrt(kn, nn):
        return sqrt(kn* (nn - 1))

    while some_n != n:
        a1 = some_sqrt(kn=k, nn=some_n)
        a2 = some_sqrt(kn=k+1, nn=some_n+1)
        mysum += a1 + a2
        some_n += 1

    return mysum


def ans3(n: int, x: float):
    '''
    x >= 3
    n >= 3
    '''
    def fac(n):
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial

    def chisl(xx, nn):
        return fac(x**(2*n-1))

    def znam(nn):
        return ((2 * nn) - 1)

    some_n = 1
    f = x

    while some_n != n:
        f -= (chisl(x, n))/(znam(n))
        some_n += 1

    return f


