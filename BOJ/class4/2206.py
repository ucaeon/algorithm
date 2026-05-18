from collections import deque

n, m = map(int, input().split())

data = []
for _ in range(n):
    a = list(map(int, input().strip()))
    data.append(a)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
q = deque()

q.append((0, 0, 0))
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, b = q.popleft()

    if x == n - 1 and y == m - 1:
        print(visited[x][y][b])
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                if visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    q.append((nx, ny, b))

            if data[nx][ny] == 1:
                if b == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][b] + 1
                    q.append((nx, ny, 1))

print(-1)