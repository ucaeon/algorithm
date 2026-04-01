INF = 10**18

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))

dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

result = 0

for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if dist[i][j] <= m:
            total += item[j]
    result = max(result, total)

print(result)