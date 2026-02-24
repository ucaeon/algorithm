n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        stack = []
        stack.append((i, j, 1, data[i][j], [(i, j)]))

        while stack:
            y, x, depth, total, visited = stack.pop()

            if depth == 4:
                if total > result:
                    result = total
                else:
                    continue

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited:
                    stack.append((ny, nx, depth + 1, total + data[ny][nx], visited + [(ny, nx)]))

        center = data[i][j]
        neigh = []

        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                neigh.append(data[ny][nx])

        if len(neigh) >= 3:
            neigh.sort(reverse=True)
            s = center + neigh[0] + neigh[1] + neigh[2]
            if s > result:
                result = s

print(result)