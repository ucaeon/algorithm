n = int(input())
data = []

for i in range(n):
    data.append(input())

data = list(set(data))
data.sort()
data.sort(key = len)

for i in data:
    print(i)