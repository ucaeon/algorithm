n = int(input())

data = [[] for _ in range(n ** 2 + 1)]
seq = []

for _ in range(n ** 2):
    a, b, c, d, e = map(int, input().split())
    data[a] = [b, c, d, e]
    seq.append(a)

sch = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for student in seq:
    best = (-1, -1, -1, -1)
    best_x, best_y = 0, 0

    for i in range(n):
        for j in range(n):
            if sch[i][j] != 0:
                continue

            stu_cnt = 0
            empty_cnt = 0

            for z in range(4):
                nx = i + dx[z]
                ny = j + dy[z]

                if 0 <= nx < n and 0 <= ny < n:
                    if sch[nx][ny] in data[student]:
                        stu_cnt += 1
                    if sch[nx][ny] == 0:
                        empty_cnt += 1

            now = (stu_cnt, empty_cnt, -i, -j)

            if now > best:
                best = now
                best_x, best_y = i, j

    sch[best_x][best_y] = student

result = 0

for i in range(n):
    for j in range(n):
        student = sch[i][j]
        cnt = 0

        for z in range(4):
            nx = i + dx[z]
            ny = j + dy[z]

            if 0 <= nx < n and 0 <= ny < n:
                if sch[nx][ny] in data[student]:
                    cnt += 1

        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)