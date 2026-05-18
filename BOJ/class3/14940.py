from collections import deque

n, m = map(int, input().split())

data = []
result = [[0] * m for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            result[i][j] = -1

        if data[i][j] == 2:
            start = (i, j)
            result[i][j] = 0

queue = deque()
queue.append(start)
visited = [[False] * m for _ in range(n)]

while queue:
    y, x = queue.popleft()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and data[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append((ny, nx))
            result[ny][nx] = result[y][x] + 1
        
for i in range(n):
    for j in range(m):
        print(result[i][j], end = ' ')
    print()