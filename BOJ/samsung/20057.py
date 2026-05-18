# 입력
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

base = [
    (-1, 1, 1), (1, 1, 1),
    (-1, 0, 7), (1, 0, 7),
    (-2, 0, 2), (2, 0, 2),
    (-1, -1, 10), (1, -1, 10),
    (0, -2, 5)
]

sand = [base]
for _ in range(3):
    sand.append([(-y, x, p) for x, y, p in sand[-1]])

x, y = n // 2, n // 2
d = 0
length = 1
answer = 0

while True:
    for _ in range(2):
        for _ in range(length):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0:
                print(answer)
                exit()

            total = data[nx][ny]
            spread = 0

            for dx_s, dy_s, p in sand[d]:
                val = (total * p) // 100
                spread += val

                sx = nx + dx_s
                sy = ny + dy_s

                if 0 <= sx < n and 0 <= sy < n:
                    data[sx][sy] += val
                else:
                    answer += val

            ax = nx + dx[d]
            ay = ny + dy[d]
            remain = total - spread

            if 0 <= ax < n and 0 <= ay < n:
                data[ax][ay] += remain
            else:
                answer += remain

            data[nx][ny] = 0
            x, y = nx, ny

        d = (d + 1) % 4
    length += 1