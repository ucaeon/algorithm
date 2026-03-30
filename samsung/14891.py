from collections import deque
 # 입력 받기
data = []
for _ in range(4):
    data.append(deque(map(int, input().strip())))

k = int(input())

# 각 톱니 방향 찾고 돌리기
for _ in range(k):
    n, d = map(int, input().split())
    n -= 1
    st = [0] * 4
    st[n] = d

    for i in range(n, 0, -1):
        if data[i][6] != data[i-1][2]:
            st[i-1] = -st[i]
        else:
            break

    for i in range(n, 3):
        if data[i][2] != data[i+1][6]:
            st[i+1] = -st[i]
        else:
            break

    for i in range(4):
        if st[i] == 1:
            data[i].rotate(1)
        elif st[i] == -1:
            data[i].rotate(-1)

score = 1
result = 0

# 점수 계산
for i in range(4):
    if data[i][0] == 1:
        result += score
    else:
        continue
    score *= 2

print(result)