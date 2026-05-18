# 입력 받기
n, m, x, y, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

commands = list(map(int, input().split()))
dice = [0] * 6


for j in commands:
    # 주사위 이동
    if j == 1:
        nx, ny = x, y + 1
    elif j == 2:
        nx, ny = x, y - 1
    elif j == 3:
        nx, ny = x - 1, y
    elif j == 4: 
        nx, ny = x + 1, y

    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
    else:
        continue

    # 주사위 방향 이동
    if j == 1:
        dice[0], dice[5], dice[1], dice[4] = dice[5], dice[1], dice[4], dice[0]
    elif j == 2:
        dice[5], dice[0], dice[4], dice[1] = dice[0], dice[4], dice[1], dice[5]
    elif j == 3:
        dice[0], dice[2], dice[1], dice[3] = dice[2], dice[1], dice[3], dice[0]
    elif j == 4: 
        dice[0], dice[3], dice[1], dice[2] = dice[3], dice[1], dice[2], dice[0]

    # 지도랑 주사위 변경 후 출력
    if data[x][y] == 0:
        data[x][y] = dice[1]
    else:
        dice[1] = data[x][y]
        data[x][y] = 0

    print(dice[0])



