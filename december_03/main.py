def ans1():
    '''
    Даны целые положительные числа. Используя только операции сложения и вычитания, найти частное от деления нацело N на K, а также остаток от деления
    '''
    n = int(input())
    k = int(input())
    i = 0
    j = k

    while n - j > k:
        j += k
        i += 1

    m = n - j

    print(f"n div k = {i}")
    print(f"n mod k = {m}")


def ans2():
    '''
    Дано целое число N(>0). Если оно является степенью числа 3, то вывести True, иначе - False
    '''

    n = int(input("Введите целое число N: "))

    flag = False

    while n > 1:
        if n % 3 != 0:
            break
        n /= 3

    if n == 1:
        flag = True

    print(flag)
