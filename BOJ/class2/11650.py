n = int(input())
data = []

for i in range(n):
    data.append(tuple(map(int, input().split())))

data.sort(key=lambda x: (x[0], x[1]))


for i, j in data:
    print(i, j)
        