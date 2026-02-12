from collections import deque

n = int(input())

data = []
for i in range(n):
    data.append(list(map(str, input())))

visited = [[False] * n for _ in range(n)]
queue = deque()
count_1 = 0
count_2 = 0
result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            queue.append((i, j))
            count_1 += 1
            color = data[i][j]

            while queue:
                y, x = queue.popleft()

                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]

                    if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and data[ny][nx] == color:
                        queue.append((ny, nx))
                        visited[ny][nx] = True

for i in range(n):
    for j in range(n):
        if data[i][j] == 'R' or data[i][j] == 'G':
            data[i][j] = 'M'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            queue.append((i, j))
            count_2 += 1
            color = data[i][j]

            while queue:
                y, x = queue.popleft()

                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]

                    if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and data[ny][nx] == color:
                        queue.append((ny, nx))
                        visited[ny][nx] = True

print(count_1, count_2)