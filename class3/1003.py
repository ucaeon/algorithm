n = int(input())


for i in range(n):
    a = int(input())
    data = [(0, 0)] * 41

    data[0] = (1, 0)
    data[1] = (0, 1)

    for j in range(2, a + 1):
        z1, o1 = data[j - 1]
        z2, o2 = data[j - 2]
        data[j] = (z1 + z2, o1 + o2)

    print(data[a][0], data[a][1])


