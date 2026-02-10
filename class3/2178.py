from collections import deque

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input())))

queue = deque()
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0
queue.append([0, 0])

while queue:
    y, x = queue.popleft()
    
    if y == n - 1 and x == m - 1:
        print(dist[n - 1][m - 1] + 1)
        break

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and dist[ny][nx] == -1 and data[ny][nx] == 1:
            dist[ny][nx] = dist[y][x] + 1
            queue.append([ny, nx])
        else:
            continue

