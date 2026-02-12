from collections import deque

m, n = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    

result = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = True
            result[i][j] = 0

while queue:
    y, x = queue.popleft()

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n  and data[ny][nx] != -1 and not visited[ny][nx]:
            result[ny][nx] = result[y][x] + 1
            visited[ny][nx] = True
            queue.append((ny, nx))

max_value = 0

for i in range(n):
    for j in range(m):
        if result[i][j] == -1 and data[i][j] == 0:
            max_value = -1
        else:
            if max_value < result[i][j] and max_value != -1:
                max_value = result[i][j]
print(max_value)