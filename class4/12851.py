from collections import deque

n, k = map(int, input().split())

MAX = 100001
dist = [-1] * MAX
cnt = [0] * MAX

q = deque()
q.append(n)
dist[n] = 0
cnt[n] = 1

while q:
    a = q.popleft()

    for i in (a - 1, a + 1, a * 2):
        if 0 <= i < MAX:
            if dist[i] == -1:
                dist[i] = dist[a] + 1
                cnt[i] = cnt[a]
                q.append(i)

            # 같은 최단거리로 또 도착
            elif dist[i] == dist[a] + 1:
                cnt[i] += cnt[a]

print(dist[k])
print(cnt[k])