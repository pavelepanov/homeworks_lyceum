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
