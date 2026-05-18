t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        data[b][a] = 1

    visited = [[False] * m for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(m):
            if not visited[j][k] and data[j][k] == 1:
                count += 1
                stack = [(j, k)]
                visited[j][k] = True

                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                while stack:
                    x, y = stack.pop()
                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]

                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and data[nx][ny] == 1:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
    print(count)
