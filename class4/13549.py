from collections import deque

n, k = map(int, input().split())

MAX = 100001
dist = [-1] * MAX

q = deque()
q.append(n)
dist[n] = 0

while q:
    a = q.popleft()

    # 순간이동
    v = a * 2
    if 0 <= v < MAX:
        if dist[v] == -1 or dist[v] > dist[a]:
            dist[v] = dist[a]
            q.appendleft(v)

    # 걷기
    for v in (a - 1, a + 1):
        if 0 <= v < MAX:
            if dist[v] == -1 or dist[v] > dist[a] + 1:
                dist[v] = dist[a] + 1
                q.append(v)

print(dist[k])