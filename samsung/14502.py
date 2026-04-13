from itertools import combinations
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
virus = []
empty = []
max_value = -1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            virus.append((i, j))
        elif data[i][j] == 0:
            empty.append((i, j))


for walls in combinations(empty, 3):
    # 벽 선택
    new_data = [row[:] for row in data]
    for wx, wy in walls:
        new_data[wx][wy] = 1

    # BFS    
    cnt = 0
    q = deque()
    visited = [[False] * m for _ in range(n)]

    for x, y in virus:
        q.append((x, y))
        visited[x][y] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and new_data[nx][ny] == 0:
                    new_data[nx][ny] = 2
                    q.append((nx, ny))
                    visited[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if new_data[i][j] == 0:
                cnt += 1
    max_value = max(max_value, cnt)

print(max_value)