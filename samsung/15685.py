# 입력
n = int(input())
dot = []
data = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    # 세대 방향 저장
    x, y, d, g = map(int, input().split())
    dirs = [d]

    for i in range(g):
        dir = []
        for j in reversed(dirs):
            dir.append((j + 1) % 4)
        dirs += dir

    # 점 표시
    data[y][x] = 1

    for i in dirs:
        x += dx[i]
        y += dy[i]
        data[y][x] = 1

# 정사각형 세기
cnt = 0
for i in range(100):
    for j in range(100):
        if data[i][j] and data[i][j+1] and data[i+1][j] and data[i+1][j+1]:
            cnt += 1

print(cnt)
    

