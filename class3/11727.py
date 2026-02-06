n = int(input())
data = [0] * (n + 1)

if n == 1:
    print(n)
elif n == 2:
    print(3)
elif n == 3:
    print(5)
else:
    data[0] = 0
    data[1] = 1
    data[2] = 3
    data[3] = 5
    for i in range(4, n + 1):
        data[i] = data[i - 1] + 2 * data[i - 2]
        
    print(data[-1] % 10007)