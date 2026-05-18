from collections import deque
from itertools import combinations
INF = 10**18

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
viruses = []
min_time = INF

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            viruses.append((i, j))

# 바이러스 조합
for virus in combinations(viruses, m):
    new_data = [row[:] for row in data]
    for vx, vy in virus:
        new_data[vx][vy] = 3
    
    # BFS
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    time = 0
    max_dist = 0
    visited = [[False] * n for _ in range(n)]

    for x, y in virus:
        q.append((x, y))
        visited[x][y] = True
        dist[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if new_data[nx][ny] == 2 or new_data[nx][ny] == 0:
                    if not visited[nx][ny]:
                        q.append((nx, ny))
                        new_data[nx][ny] = 3
                        dist[nx][ny] = (dist[x][y] + 1)
                        visited[nx][ny] = True

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                if dist[i][j] == -1:
                    max_dist = INF
                    break
                max_dist = max(max_dist, dist[i][j])
        if max_dist == INF:
            break

    min_time = min(max_dist, min_time)

if min_time == INF:
    print(-1)
else:
    print(min_time)
                