from collections import deque

n, m, v = map(int, input().split())
data = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(1, n + 1):
    data[i].sort()

visited = [False] * (n + 1)
stack = [v]
r_stack = []

while stack:
    a = stack.pop()
    if visited[a]:
        continue

    visited[a] = True
    r_stack.append(a)

    for i in reversed(data[a]):
        if not visited[i]:
            stack.append(i)


visited = [False] * (n + 1)
queue = deque()
queue.append(v)
visited[v] = True
r_queue = []


while queue:
    a = queue.popleft()
    r_queue.append(a)

    for i in data[a]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

for i in r_stack:
    print(i, end = ' ')
print()
for i in r_queue:
    print(i, end = ' ')
