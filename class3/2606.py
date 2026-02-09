n = int(input())
m = int(input())

data = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n + 1)
start = 1
stack = [start]
count = 0

while stack:
    i = stack.pop()

    if visited[i]:
        continue
    visited[i] = True
    count += 1

    for j in reversed(data[i]):
        if not visited[j]:
            stack.append(j)

print(count - 1)


