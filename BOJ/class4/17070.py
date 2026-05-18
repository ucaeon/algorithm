n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(n)]

# 가로:0, 세로:1, 대각:2
dp[0][1][0] = 1

for c in range(n):
    for r in range(n):
        if data[c][r] == 1:
            continue

        # 가로
        if 0 <= c < n and 0 <= (r - 1) < n: 
            dp[c][r][0] += dp[c][r - 1][0]
            dp[c][r][0] += dp[c][r - 1][2]
        else:
             continue

        # 세로
        if 0 <= (c - 1) < n and 0 <= r < n: 
            dp[c][r][1] += dp[c - 1][r][1]
            dp[c][r][1] += dp[c - 1][r][2]
        else:
             continue

        # 대각선
        if 0 <= (c - 1) < n and 0 <= (r - 1) < n: 
            if data[c - 1][r] == 0 and data[c][r - 1] == 0 and data[c - 1][r - 1] == 0:
                dp[c][r][2] += dp[c - 1][r - 1][0]
                dp[c][r][2] += dp[c - 1][r - 1][1]
                dp[c][r][2] += dp[c - 1][r - 1][2]
        else:
             continue

# 출력
result = sum(dp[n - 1][n - 1])
if result == 0:
    print(0)
else:
    print(result)