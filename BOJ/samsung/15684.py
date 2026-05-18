# 입력
n, m, h = map(int, input().split())
data = [[0] * n for _ in range(h)]

answer = 4

for _ in range(m):
    a, b = map(int, input().split())
    data[a - 1][b - 1] = 1

def dfs(cnt, start):
    global answer

    if cnt >= answer:
        return

    # 사다리 검사
    ok = True
    for s in range(n):
        cur = s

        for i in range(h):
            if cur < n - 1 and data[i][cur] == 1:
                cur += 1
            elif cur > 0 and data[i][cur - 1] == 1:
                cur -= 1
        if cur != s:
            ok = False
            break
    if ok:
        answer = cnt
        return

    if cnt == 3:
        return

    for num in range(start, h * (n - 1)):
        x = num // (n - 1)
        y = num % (n - 1)

        if data[x][y] == 1:
            continue
        if y > 0 and data[x][y - 1] == 1:
            continue
        if y < n - 2 and data[x][y + 1] == 1:
            continue

        data[x][y] = 1
        dfs(cnt + 1, num + 1)
        data[x][y] = 0

dfs(0, 0)

if answer == 4:
    print(-1)
else:
    print(answer)