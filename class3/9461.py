n = int(input())

for i in range(n):
    a = int(input())
    data = [0] * (a + 1)

    if a <= 3:
        print(1)
    else:
        data[0] = 0
        data[1] = 1
        data[2] = 1
        data[3] = 1

        for j in range(4, a + 1):
            data[j] = data[j - 3] + data[j - 2]

        print(data[a])
