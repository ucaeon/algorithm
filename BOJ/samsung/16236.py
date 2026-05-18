from collections import deque

# 입력
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y = 0, 0
size = 2
eat = 0
ans = 0

# 아기상어 위치
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            x, y = i, j
            data[i][j] = 0

while True:
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    fish = []

    # 먹을 수 있는 물고기 찾기
    while q:
        a, b, dist = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and data[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

                    if 0 < data[nx][ny] < size:
                        fish.append((dist + 1, nx, ny))

    if len(fish) == 0:
        break

    fish.sort()
    dist, x, y = fish[0]

    ans += dist
    eat += 1
    data[x][y] = 0

    if eat == size:
        size += 1
        eat = 0

print(ans)