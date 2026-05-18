# 입력 받기
n, k = map(int, input().split())
data = []
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

# 모든 경우의 수 중 최댓값 dp에 저장
for i in range(1, n + 1):
    w, value = data[i - 1]
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]

        if j >= w:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + value)

print(dp[n][k])




