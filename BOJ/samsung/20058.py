from collections import deque

# 입력
n, q = map(int, input().split())
size = 2 ** n

data = [list(map(int, input().split())) for _ in range(size)]
level = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for l in level:
    step = 2 ** l
    board = [[0] * size for _ in range(size)]

    # 부분 격자 회전
    for x in range(0, size, step):
        for y in range(0, size, step):
            for i in range(step):
                for j in range(step):
                    board[x + j][y + step - 1 - i] = data[x + i][y + j]
    data = board

    # 얼음 줄이기
    melt = []

    for i in range(size):
        for j in range(size):
            if data[i][j] == 0:
                continue
            cnt = 0

            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]

                if 0 <= nx < size and 0 <= ny < size:
                    if data[nx][ny] > 0:
                        cnt += 1
            if cnt < 3:
                melt.append((i, j))
    for x, y in melt:
        data[x][y] -= 1

# 얼음 더하기
ans = 0
for i in range(size):
    ans += sum(data[i])

# 가장 큰 얼음 덩어리
visited = [[False] * size for _ in range(size)]
big = 0

for i in range(size):
    for j in range(size):
        if data[i][j] > 0 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            cnt = 1

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < size and 0 <= ny < size:
                        if data[nx][ny] > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cnt += 1

            big = max(big, cnt)

print(ans)
print(big)