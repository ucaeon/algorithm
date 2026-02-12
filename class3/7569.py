from collections import deque

m, n, h = map(int, input().split())

data = []
for i in range(h):
    layer = []
    for j in range(n):
        layer.append(list(map(int, input().split())))
    data.append(layer)

result = [[[-1] * m for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for z in range(m):
            if data[i][j][z] == 1:
                queue.append((i, j, z))
                visited[i][j][z] = True
                result[i][j][z] = 0

while queue:
    z, y, x = queue.popleft()

    dz = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [1, -1, 0, 0, 0, 0]

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and data[nz][ny][nx] != -1 and not visited[nz][ny][nx]:
            result[nz][ny][nx] = result[z][y][x] + 1
            visited[nz][ny][nx] = True
            queue.append((nz, ny, nx))

max_value = 0

for i in range(h):
    for j in range(n):
        for z in range(m):
            if result[i][j][z] == -1 and data[i][j][z] == 0:
                max_value = -1
            else:
                if max_value < result[i][j][z] and max_value != -1:
                    max_value = result[i][j][z]
print(max_value)