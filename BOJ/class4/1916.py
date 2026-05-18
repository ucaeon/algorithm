import heapq

n = int(input())
m = int(input())

INF = 10**18

data = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))

s, e = map(int, input().split())

d = [INF] * (n + 1)
d[s] = 0

pq = []
heapq.heappush(pq, (0, s))

while pq:
    dist, now = heapq.heappop(pq)

    if d[now] < dist:
        continue
    else:
        for a, b in data[now]:
            nd = dist + b

            if nd < d[a]:
                d[a] = nd
                heapq.heappush(pq, (nd, a))

print(d[e])
