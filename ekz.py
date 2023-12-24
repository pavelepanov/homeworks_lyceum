def ans():
    def znam(a):
        return ((a * 2) ** 2)

    n = int(input())
    mysum = 0
    for i in range(1, n+1):
        mysum += 1/(znam(i))

    return mysum


def ans2():
    from math import factorial
    return factorial(4)


def ans3():
    from math import sqrt
    def mysqrt(n):
        return sqrt(n)
    mysum = 0
    for i in range(50):
        mysum += mysqrt(i)

    return mysum


def ans59():
    n = int(input())
    m = []
    c = {}

    minsum = 99999999999999999999

    for i in range(n):
        a = int(input())
        m.append(a)

    u1 = 0
    u2 = 1
    ab1 = 'one'
    ab2 = 'two'
    #c[str(m[u1])] = m[u1]
    #c[str(m[u2])] = m[u2]
    #minsum = c[str(m[u1])] + c[str(m[u2])]

    for i in range(len(m)-1):
        if m[u1] + m[u2] < minsum:
            c[ab1] = u1 - 1
            c[ab2] = u2 - 1
            minsum = m[u1] + m[u2]
        u1 += 1
        u2 += 1



    return c

print(ans59())
