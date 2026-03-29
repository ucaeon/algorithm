# 입력 받기
n, m = map(int, input().split())
x, y, d = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

cnt = 0
dic = [0, 1, 2, 3]
visited = [[False] * m for _ in range(n)]

while True:
    move = False

    # 현재 칸 청소
    if data[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        cnt += 1

    # 동서남북 확인
    for _ in range(4):
        d = (d + 3) % 4

        if d == 0:
            nx, ny = x - 1, y
        elif d == 1:
            nx, ny = x, y + 1
        elif d == 2:
            nx, ny = x + 1, y
        elif d == 3:
            nx, ny = x, y - 1

        if data[nx][ny] == 0 and visited[nx][ny] == False:
            x, y = nx, ny
            move = True
            break
    
    # 이동 못하면 뒤로 한칸
    if not move:
        back = (d + 2) % 4

        if back == 0:
            nx, ny = x - 1, y
        elif back == 1:
            nx, ny = x, y + 1
        elif back == 2:
            nx, ny = x + 1, y
        elif back == 3:
            nx, ny = x, y - 1

        if data[nx][ny] == 1:
            print(cnt)
            break
        else:
            x, y = nx, ny