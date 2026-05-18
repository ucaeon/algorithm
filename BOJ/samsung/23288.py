from collections import deque

# 입력
n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 주사위
top = 1
bottom = 6
left = 4
right = 3
front = 5
back = 2

x, y = 0, 0
d = 0
ans = 0

for _ in range(k):
    nx = x + dx[d]
    ny = y + dy[d]

    # 범위 밖이면 반대 방향
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    x, y = nx, ny

    # 주사위 굴리기
    if d == 0:      # 동
        top, bottom, left, right = left, right, bottom, top
    elif d == 1:    # 남
        top, bottom, front, back = back, front, top, bottom
    elif d == 2:    # 서
        top, bottom, left, right = right, left, top, bottom
    elif d == 3:    # 북
        top, bottom, front, back = front, back, bottom, top

    # 점수 계산 BFS
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    cnt = 1
    num = data[x][y]

    while q:
        a, b = q.popleft()

        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]

            if 0 <= na < n and 0 <= nb < m:
                if not visited[na][nb] and data[na][nb] == num:
                    visited[na][nb] = True
                    q.append((na, nb))
                    cnt += 1

    ans += cnt * num

    # 방향 변경
    if bottom > data[x][y]:
        d = (d + 1) % 4
    elif bottom < data[x][y]:
        d = (d + 3) % 4

print(ans)