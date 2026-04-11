from collections import deque

# 입력
n = int(input())
k = int(input())

data = [[0] * (n + 1) for _ in range(n + 1)]
tlist = deque()
moved = deque()
time = 0
dir = 1
moved.append((1, 1))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())

for _ in range(l):
    a, b = map(str, input().split())
    tlist.append((int(a), b))

while True:
    # 이동
    x, y = moved[-1]
    nx = x + dx[dir]
    ny = y + dy[dir]
    time += 1

    # 종료조건
    if nx < 1 or ny < 1 or nx > n or ny > n:
        break
    if (nx, ny) in moved:
        break

    # 방향 변경
    if tlist and tlist[0][0] == time:
        t, d = tlist.popleft()
        if d == 'D':
            dir = (dir + 1) % 4
        elif d == 'L':
            dir = (dir - 1) % 4

    # 사과 확인
    moved.append((nx, ny))

    if data[nx][ny] == 1:
        data[nx][ny] = 0
    else:
        moved.popleft()

print(time)











        
