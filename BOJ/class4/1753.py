import heapq

n, m = map(int, input().split())
s = int(input())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))

INF = 10**18
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

            if nd < d[e]:
                d[e] = nd
                heapq.heappush(pq, (nd, e))

for i in range(1, len(d)):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])
