import heapq

n = int(input())
m = int(input())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))

s, e = map(int, input().split())

INF = 10**18
d = [INF] * (n + 1)
d[s] = 0

pq = []
heapq.heappush(pq, (0, s))

seq = [0] * (n + 1)

while pq:
    dist, now = heapq.heappop(pq)

    if d[now] < dist:
        continue
    else:
        for node, v in data[now]:
            nd = dist + v
            
            if d[node] > nd:
                d[node] = nd
                seq[node] = now
                heapq.heappush(pq, (nd, node))

result = []
end = e

while end != 0:
    result.append(end)
    end = seq[end]
result.reverse()

print(d[e])
print(len(result))
print(*result)