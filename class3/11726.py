a = int(input())
data = [0] * (a + 1)

if a <= 2:
    print(a)
else:
    data[0] = 0
    data[1] = 1
    data[2] = 2
    data[3] = 3

    for j in range(4, a + 1):
        data[j] = data[j - 1] + data[j - 2]

    print(data[-1] % 10007)
