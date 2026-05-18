import math
n = int(input())
sq = []
data = [0] * (n + 1)

for i in range(1, int(math.sqrt(n)) + 1):
    sq.append(i**2)

for i in range(1, n + 1):
    m = []
    for j in sq:
        if j <= i:
            m.append(data[i - j] + 1)
        else:
            break
    data[i] = min(m)

print(data[n])
