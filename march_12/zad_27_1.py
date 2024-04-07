'''
a - 22336
'''

def find_max(ml, k):
    mysum = 0
    counter = 0
    for value in range(len(ml) - 420):
        myind = counter
        for i in range(3):
            if ml[myind] + ml[myind + k] + ml[myind + k * 2] > mysum:
                mysum = ml[myind] + ml[myind + k] + ml[myind + k * 2]
        counter += 3
    print(mysum)

def find_max_sum(sequence, k):
    a1 = 0
    a2 = 1
    a3 = 2
    mysum = 0
    for value in range(len(sequence) - 250):
        if sequence[a1] + sequence[a1 + k] + sequence[a1 + k * 2] > mysum:
            mysum = sequence[a1] + sequence[a1 + k] + sequence[a1 + k * 2]
        a1 += 1

    print(mysum)

def new_max(seq, k):
    mysum = 0
    for i in range(len(seq) - 200):
        if seq[i] + seq[i + 1 + k] + seq[i + 2 + k] > mysum:
            mysum = seq[i] + seq[i + 1 + k] + seq[i + 2 + k]
    print(mysum)

def some_max(seq, k):
    a1 = 0
    a2 = 1
    a3 = 2
    matrix = []
    mysum = 0
    for i in range(len(seq) - 3):
        matrix.append([seq[a1], seq[a2], seq[a3]])
        a1 += 1
        a2 += 1
        a3 += 1
    ind = 0
    for value in range(len(seq) - 124):
        c1 = seq[ind]
        c2 = seq[ind+k]
        c3 = seq[ind+1+k]
        if c1 + c2 + c3 > mysum:
            mysum = c1 + c2 + c3
        ind += 1
    print(mysum)



with open('a1.txt', 'r') as file:
    a = file.read().split()
    k1 = int(a[1])
    a1 = []
    a1.append(a[0])
    a1 = a[2:]
    a1 = list(map(int, a1))
    #find_max(a1, k1)
    #find_max_sum(a1, k1)
    #new_max(a1, k1)
    some_max(a1, k1)


with open('b1.txt', 'r') as file:
    b = file.read().split()
    k2 = int(b[1])
    b1 = []
    b1.append(b[0])
    b1 = b[2:]
    b1 = list(map(int, b1))
