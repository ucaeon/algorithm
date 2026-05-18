from collections import deque

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
days = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while True:
    moved = False
    q = deque()
    visited = [[False] * n for _ in range(n)]
    new_data = [row[:] for row in data]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                part = []
                cnt = 0
                total = 0

                visited[i][j] = True
                q.append((i, j))
                cnt += 1
                total += data[i][j]
                part.append((i, j))

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny]:
                                if l <= abs(data[x][y] - data[nx][ny]) <= r:
                                    q.append((nx, ny))
                                    visited[nx][ny] = True
                                    cnt += 1
                                    total += data[nx][ny]
                                    part.append((nx, ny))

                for px, py in part:
                    n_value = (total // cnt)
                    new_data[px][py] = n_value
                if cnt > 1:
                    moved = True
    if not moved:
        break
    data = new_data
    days += 1

print(days)
