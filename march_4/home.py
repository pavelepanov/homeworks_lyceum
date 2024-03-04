def ans361():
    a = int(input())
    c = []
    mysum = 0
    for i in range(a):
        r = list(map(int, input().split()[1:]))
        c.append(r)
    n = int(input())
    for j in c:
        mysum += j[n-1]

    print(int(mysum/a))

def ans362():
    categories = {"отлично": [8, 9, 10],
    "хорошо": [5, 6, 7],
    "удовлетворительно": [3, 4],
    "неудовлетворительно": [0, 1, 2]}

    a = int(input())
    c = []
    mysum = 0
    for i in range(a):
        r = list(map(int, input().split()[1:]))
        c.append(r)
    n = int(input())
    for j in c:
        mysum += j[n-1]

    sred = int(mysum/a)
    for key, value in categories.items():
        if sred in value:
            print(key)
