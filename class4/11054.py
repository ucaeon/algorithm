# 입력 받기
n = int(input())
data = list(map(int, input().split()))

front = [1] * n
back = [1] * n
result = [0] * n

# 앞 바이토닉 수열 최대 구하기
for i in range(len(data)):
    count = 1
    for j in range(i):
        if data[j] < data[i]:
            front[i] = max(front[i], front[j] + 1)

# 뒤 바이토닉 수열 최대 구하기
for i in range(len(data) - 1, -1, -1):
    count = 1
    for j in range(len(data) - 1, i, -1):
        if data[j] < data[i]:
            back[i] = max(back[i], back[j] + 1)

# 두 dp 더해서 최대 길이 찾기
for i in range(n):
    result[i] = front[i] + back[i] - 1

print(max(result))


