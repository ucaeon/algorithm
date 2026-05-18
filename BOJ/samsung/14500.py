n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for col in range(n):
    for row in range(m):
        # ㅗ 모양 제외 나머지(DFS로 가능)
        stack = []
        stack.append((col, row, 1, board[col][row], [(col, row)]))

        while stack:
            x, y, dep, total, visited = stack.pop()

            if dep == 4:
                if result < total:
                    result = total
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in visited:
                        stack.append((nx, ny, dep + 1, total + board[nx][ny], visited + [(nx, ny)]))
        
        # ㅗ 모양
        center = board[col][row]
        near = []

        for i in range(4):
            nx = col + dx[i]
            ny = row + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                near.append(board[nx][ny])

            if len(near) >= 3:
                total = center + sum(near)
                if len(near) == 4:
                    total -= min(near)

                result = max(result, total)

print(result)
