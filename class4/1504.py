import heapq

n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

v1, v2 = map(int, input().split())
s = 1
e = n

INF = 10**18

def dijkstra(start):
    d = [INF] * (n + 1)
    d[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        if d[now] < dist:
            continue

        for nxt, cost in data[now]:
            nd = dist + cost

            if nd < d[nxt]:
                d[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return d

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

result1 = d1[v1] + d2[v2] + d3[n]
result2 = d1[v2] + d3[v1] + d2[n]
result = min(result1, result2)

if result >= INF:
    print(-1)
else:
    print(result)
