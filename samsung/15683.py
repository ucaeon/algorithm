# 입력
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cctv = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 10**9

direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

for i in range(n):
    for j in range(m):
        if 1 <= data[i][j] <= 5:
            cctv.append((i, j, data[i][j]))

def dfs(depth):
    global answer

    if depth == len(cctv):
        cnt = 0

        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    cnt += 1

        answer = min(answer, cnt)
        return

    x, y, num = cctv[depth]

    for dirs in direction[num]:
        changed = []

        for d in dirs:
            nx = x + dx[d]
            ny = y + dy[d]

            while 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 6:
                    break
                if data[nx][ny] == 0:
                    data[nx][ny] = -1
                    changed.append((nx, ny))
                nx += dx[d]
                ny += dy[d]

        dfs(depth + 1)

        for cx, cy in changed:
            data[cx][cy] = 0

dfs(0)
print(answer)