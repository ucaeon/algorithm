from collections import deque

# 입력, 변수 정의
n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
food = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    trees[a - 1][b - 1].append(c)

for x in range(n):
    for y in range(n):
        trees[x][y] = deque(sorted(trees[x][y]))

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1 ]

for i in range(k):
    # 봄
    for x in range(n):
        for y in range(n):
            live = deque()
            dead_sum = 0
            cell = trees[x][y]

            for idx in range(len(cell)):
                if cell[idx] <= food[x][y]:
                    food[x][y] -= cell[idx]
                    live.append(cell[idx] + 1)
                else: 
                    # 여름
                    for die in range(idx, len(cell)):
                        dead_sum += (cell[die] // 2)
                    break
            trees[x][y] = live
            food[x][y] += dead_sum     

    # 가을   
    for x in range(n):
        for y in range(n):
            for age in trees[x][y]:
                if age % 5 == 0:
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)

    # 겨울
    for x in range(n):
        for y in range(n):
            food[x][y] += data[x][y]

# 개수 세기
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])
print(cnt)

