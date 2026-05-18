# 입력
n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

def check(line):
    used = [False] * n

    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue

        # 높이 차 1 초과
        if abs(line[i] - line[i + 1]) > 1:
            return False

        # 내려가는 경우
        if line[i] - line[i + 1] == 1:
            h = line[i + 1]
            for j in range(i + 1, i + 1 + l):
                if j >= n or line[j] != h or used[j]:
                    return False
                used[j] = True

        # 올라가는 경우
        elif line[i + 1] - line[i] == 1:
            h = line[i]
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != h or used[j]:
                    return False
                used[j] = True

    return True


# 결과
ans = 0

# 행 체크
for i in range(n):
    if check(data[i]):
        ans += 1

# 열 체크
for j in range(n):
    col = []
    for i in range(n):
        col.append(data[i][j])
    if check(col):
        ans += 1

print(ans)