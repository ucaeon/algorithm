from collections import deque

# 입력 받기 / 정의
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

form = []
for _ in range(m):
    a, b = map(int, input().split())
    form.append((a, b))

cloud = deque()
cloud.extend([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for seq in range(m):
    board = [row[:] for row in data]
    visited = [[False] * n for _ in range(n)]
    n_cloud = deque()

    # 구름 이동
    d, s = form[seq]
    dx = [0, -s, -s, -s, 0, s, s, s]
    dy = [-s, -s, 0, s, s, s, 0, -s]

    for _ in range(len(cloud)):
        x, y = cloud.popleft()
        nx = (x + dx[d - 1] + n) % n
        ny = (y + dy[d - 1] + n) % n

        visited[nx][ny] = True
        n_cloud.append((nx, ny))

    # 물 증가
    for r, c in n_cloud:
        board[r][c] += 1

    # 물복사버그 마법
    diag_x = [-1, -1, 1, 1]
    diag_y = [-1, 1, -1, 1]

    for x, y in n_cloud:
        cnt = 0
        for k in range(4):
            nx = x + diag_x[k]
            ny = y + diag_y[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] > 0:
                    cnt += 1
        board[x][y] += cnt

    # 새 구름 만들기
    cloud = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not visited[i][j]:
                cloud.append((i, j))
                board[i][j] -= 2
    data = board

# 결과 출력
answer = 0
for i in range(n):
    answer += sum(data[i])
print(answer)