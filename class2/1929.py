from math import sqrt

a, b = map(int, input().split())

data = [True] * (b + 1)

for i in range(2, int(sqrt(b)) + 1):
    if data[i]:
        j = 2
        while i * j <= b:
            data[i * j] = False
            j += 1

data[0] = False
data[1] = False
for i in range(a, b + 1):
    if data[i]:
        print(i)