n, m = map(int, input().split())

data = {}
result = []

for i in range(n):
    a, b = map(str, input().split())
    data[a] = b

for i in range(m):
    v = input().strip()
    if v in data:
        result.append(data[v])

for i in result:
    print(i)



