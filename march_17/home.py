def ans1():
    a = 0
    b = 0
    m = [
            [1, 2, 3, 4],
            [0, 0, 0, 0],
            [5, 6, 7, 8],
            [0, 0, 0, 0],
        ]
    for i in m:
        for j in i:
            if j != 0:
                a = 1
                break
        if a != 1:
            b += 1
        a = 0
    print(b)


def ans2():
    a = 0
    b = 0
    m = [
            [1, 2, 3, 4],
            [0, 0, 0, 0],
            [5, 6, 7, 8],
            [0, 0, 0, 0],
        ]
    for i in m:
        if 0 in i:
            a += 1
        if a != 1:
            b += 1
        a = 0
    print(b)


def ans3():
    a = 0
    b = 0
    m = [
            [1, 2, 3, 4],
            [0, 0, 0, 0],
            [5, 6, 7, 8],
            [0, 0, 0, 0],
        ]
    for i in m:
        if 0 not in i:
            a += 1
        if a != 1:
            b += 1
        a = 0
    print(b)


def ans4():
    m = [
            [1, 2, 3, 4],
            [0, 0, 0, 6],
            [5, 0, 0, 8],
            [0, 0, 0, 6],
            [0, 3, 3, 9]
        ]
    num_columns = len(m[0])
    count = 0
    for col in range(num_columns):
        zero_count = 0
        for row in range(len(m)):
            if m[row][col] == 0:
                zero_count += 1
        if zero_count > len(m) / 2:
            count += 1
    print(count)

def ans5():
    m = [
            [1, 2, 3, 4],
            [0, 0, 0, 6],
            [5, 0, 0, 8],
            [0, 0, 0, 6],
            [0, 3, 3, 9],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
    l = [1 for i in range(int(len(m[0])))]
    ans = 0
    for j in m:
        if j == l:
            ans += 1

    print(ans)


def ans6():
    m = [
            [1, 2, 3, 4],
            [0, 0, 0, 6],
            [5, 0, 0, 8],
            [0, 0, 0, 6],
            [0, 3, -3, 9],
            [-1, 1, 1, 1],
            [-1, 1, 1, 1]
        ]
    a = 0
    for row in m:
        for col in row:
            if col < 0:
                break
        else:
            a += 1

    print(a)

def ans7():
    m = [
            [1, 2, -3, 4],
            [0, 0, -4, 6],
            [5, 0, -54, 8],
            [-1, 1, -1, 1],
            [-6, -6, -6, -6],
            [7, 7, -313, 1]
        ]
    columns = []
    for col in range(len(m[0])):
        for row in range(len(m)):
            if m[row][col] > 0:
                columns.append(col)
                break
    print(columns)

def ans8():
    m = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]

    a = 0
    for i in m:
        a += sum(i)
    if a == 0:
        print(True)
    else:
        print(False)

def ans9():
    m = [
        [0, 0, 2],
        [0, 0, 0],
        [0, 0, 1]
    ]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j and m[i][j] != 0:
                return False
    return True


def ans10():
    m = [
        [1, 0, 1],
        [0, 1, 0],
        [5, 0, 1]
    ]
    giag = None
    anot = None
    for row in range(len(m)):
        for col in range(len(m)):
            if row == col:
                if m[row][col] == 1:
                    print(m[row][col])
                    diag = True
                else:
                    diag = False
                    break
        if not diag:
            break
    print(diag)

def ans11():
    m = [
        [1, 0, 2],
        [0, 1, 0],
        [0, 0, 0],
    ]

    nula = []
    a = 0
    for row in m:
        for col in row:
            if col == 0:
                a += 1
        else:
            nula.append(a)
            a = 0

    if nula == list(sorted(nula)):
        print(True)
    else:
        print(False)

def ans12():
    m = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3],
    ]
    nula = []

    for row in m:
        nula.append(sum(row))
    if nula == list(sorted(nula)):
        print(True)
    else:
        print(False)


def ans13():
    m = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 1],
    ]
    nula = [0 for i in range(len(m[0]))]

    for col in range(len(m[0])):
        for row in range(len(m)):
            nula[col] += m[row][col]
    if nula == nula[::-1]:
        print(True)
    else:
        print(False)


def ans14():
    m = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    nula = [0 for i in range(len(m[0]))]

    for col in range(len(m[0])):
        for row in range(len(m)):
            nula[col] += m[row][col]

    if len(set(nula)) == 1:
        print(True)
    else:
        print(False)


def ans15():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    matrix = [
        [2, 3, 5, 7],
        [8, 11, 13, 17],
        [19, 23, 29, 31],
        [37, 41, 43, 47]
    ]


    rows, cols = len(matrix), len(matrix[0])
    primes = []
    for i in range(rows):
        for j in range(cols):
            if is_prime(matrix[i][j]):
                primes.append((matrix[i][j], i, j))

    triangles_count = 0
    for a in primes:
        x1, y1 = a[1], a[2]
        for b in primes:
            if a == b:
                continue
            x2, y2 = b[1], b[2]
            v1 = (x2 - x1, y1 - y2)  # вектор между a и b
            a_mirror = (x1 + v1[1], y1 + v1[0])  # зеркально отраженная точка a
            if a_mirror in primes:
                c = (x2 + v1[1], y2 + v1[0])  # третья вершина треугольника
                if c in primes:
                    triangles_count += 1

    print(triangles_count)



ans15()
