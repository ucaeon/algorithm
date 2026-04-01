import heapq

n, m, s = map(int, input().split())

data1 = [[] for _ in range(n + 1)]
data2 = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data1[a].append((b, c))
    data2[b].append((a, c))

INF = 10**18

def dijkstra(data):
    d = [INF] * (n + 1)
    d[s] = 0

    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        dist, now = heapq.heappop(pq)

        if d[now] < dist:
            continue
        else:
            for e, v in data[now]:
                nd = dist + v

                if d[e] > nd:
                    d[e] = nd
                    heapq.heappush(pq, (nd, e))

    return d

result1 = dijkstra(data1)
result2 = dijkstra(data2)

result = 0

for i in range(1, n + 1):
    a = result1[i] + result2[i]
    if result < a:
        result = a

print(result)
