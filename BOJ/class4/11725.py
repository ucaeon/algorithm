from collections import deque

n = int(input())

data = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

result = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
q = deque()
q.append(1)

while q:
    x = q.popleft()

    for j in data[x]:
        if not visited[j]:
            visited[j] = True
            result[j] = x
            q.append(j)

for i in result:
    if i != 0:
        print(i)
