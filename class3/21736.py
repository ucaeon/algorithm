from collections import deque

data = []
n, m = map(int, input().split())
for i in range(n):
    data.append(list(map(str, input())))

visited = [[False] * m for _ in range(n)]
result = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 'I':
            visited[i][j] = True
            queue.append((i, j))

while queue:
    y, x = queue.popleft()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < m and 0 <= ny < n:
            if data[ny][nx] == 'P' and visited[ny][nx] == False:
                result += 1
                queue.append((ny, nx))
                visited[ny][nx] = True
            elif data[ny][nx] == 'O' and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True
            else:
                continue
        else:
            continue

if result:
    print(result)
else:
    print('TT')


     




