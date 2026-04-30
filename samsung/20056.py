# 입력
n, m, k = map(int, input().split())

fb = []
for _ in range(m):
    r, c, mm, s, d = map(int, input().split())
    fb.append((r - 1, c - 1, mm, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    bd = [[[] for _ in range(n)] for _ in range(n)]

    # 이동
    for x, y, mm, s, d in fb:
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        bd[nx][ny].append((mm, s, d))

    fb = []

    # 합치기
    for i in range(n):
        for j in range(n):
            if not bd[i][j]:
                continue
            if len(bd[i][j]) == 1:
                fb.append((i, j, *bd[i][j][0]))
                continue

            sm = 0
            ss = 0
            even = 0
            odd = 0

            for mm, s, d in bd[i][j]:
                sm += mm
                ss += s
                if d % 2 == 0:
                    even += 1
                else:
                    odd += 1
            nm = sm // 5

            if nm == 0:
                continue
            ns = ss // len(bd[i][j])

            if even == 0 or odd == 0:
                nd = [0, 2, 4, 6]
            else:
                nd = [1, 3, 5, 7]
            for d in nd:
                fb.append((i, j, nm, ns, d))

# 출력
ans = 0
for i in fb:
    ans += i[2]
print(ans)