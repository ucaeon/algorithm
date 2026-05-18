n = int(input())
data = [0] * (n + 1)

if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    data[2] = 1
    data[3] = 1

    for i in range(4, n + 1):
        data[i] = data[i - 1] + 1

        if i % 2 == 0:
            data[i] = min(data[i // 2] + 1, data[i])
        
        if i % 3 == 0:
            data[i] = min(data[i // 3] + 1, data[i])
    print(data[n])