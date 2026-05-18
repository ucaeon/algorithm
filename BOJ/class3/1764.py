import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = set()
count = 0
result = []

for i in range(n):
    x = input().strip()
    data.add(x)

for i in range(m):
    y = input().strip()
    if y in data:
        count += 1
        result.append(y)
    else:
        continue

print(count)
result.sort()
for i in result:
    print(i)