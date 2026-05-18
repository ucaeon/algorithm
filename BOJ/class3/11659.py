n, m = map(int, input().split())
data = list(map(int, input().split()))

total = 0
sl = [0]
for i in data:
    total += i
    sl.append(total)

result = []

for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    result.append(sl[b + 1] - sl[a])

for i in result:
    print(i)
