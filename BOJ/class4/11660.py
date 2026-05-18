n, m = map(int, input().split())

data = []
result = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + data[i-1][j-1]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    result.append(dp[y2][x2] - dp[y1 - 1][x2] - dp[y2][x1 - 1] + dp[y1 - 1][x1 - 1])

for i in result:
    print(i)
