n = int(input())
data = []

for i in range(n):
    data.append(list(map(str, input().split())))

data.sort(key = lambda x : int(x[0]))

for i, j in data:
    print(i, j)