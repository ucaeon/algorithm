from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# visited에 외부 공기만 True로 저장
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and data[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return visited

# 치즈 녹이기
def find_melt(visited):
    melt = []

    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                cnt = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if visited[nx][ny]:
                            cnt += 1

                if cnt >= 2:
                    melt.append((i, j))
    return melt

time = 0

# 메인
while True:
    visited = bfs()
    melt = find_melt(visited)

    if not melt:
        break
    for x, y in melt:
        data[x][y] = 0
    time += 1

print(time)



