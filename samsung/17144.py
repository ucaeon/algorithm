r, c, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]
up = 0
down = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 공기청정기 찾기
for x in range(r):
    if data[x][0] == -1:
        up = x
        down = x + 1
        break

for i in range(t):
    temp = [[0] * c for _ in range(r)]
    temp[up][0] = -1
    temp[down][0] = -1

    # 미세먼지 확산
    for x in range(r):
        for y in range(c):
            if data[x][y] > 0:
                d_cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < r and 0 <= ny < c:
                        if data[nx][ny] != -1:
                            d_cnt += 1
                            temp[nx][ny] += (data[x][y] // 5)
                temp[x][y] += data[x][y] - ((data[x][y] // 5) * d_cnt)
    
    # 공기청정기 작동(위쪽)
    for move in range(up - 1, 0, -1):
        temp[move][0] = temp[move - 1][0]
    for move in range(c - 1):
        temp[0][move] = temp[0][move + 1]
    for move in range(up):
        temp[move][c - 1] = temp[move + 1][c - 1]
    for move in range(c - 1, 1, -1):
        temp[up][move] = temp[up][move - 1]
    temp[up][1] = 0
    temp[up][0] = -1

    # 공기청정기 작동(아래쪽)
    for move in range(down + 1, r - 1):
        temp[move][0] = temp[move + 1][0]
    for move in range(c - 1):
        temp[r - 1][move] = temp[r - 1][move + 1]
    for move in range(r - 1, down, -1):
        temp[move][c - 1] = temp[move - 1][c - 1]
    for move in range(c - 1, 1, -1):
        temp[down][move] = temp[down][move - 1]
    temp[down][1] = 0
    temp[down][0] = -1

    # 데이터 갱신
    data = [row[:] for row in temp]

cnt = 0
for x in range(r):
    for y in range(c):
        if data[x][y] > 0:
            cnt += data[x][y]
print(cnt)
        