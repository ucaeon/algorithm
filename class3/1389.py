from collections import deque

n, m = map(int, input().split())
data = [[] for i in range (n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b) 
    data[b].append(a)

queue = deque()
result = [0] * (n + 1)

for i in range(1, n + 1):
    dist = [-1] * (n + 1)
    dist[i] = 0
    queue.append(i)

    while queue:
        a = queue.popleft()

        for j in data[a]:
            if dist[j] == -1:
                dist[j] = dist[a] + 1
                queue.append(j)

    result[i] = sum(dist[1:])

total = result.index(min(result[1:]))
print(total)


  







