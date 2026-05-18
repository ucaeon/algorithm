a = int(input())
dp = [[0] * 15 for i in range(15)]

for i in range(1, 15):
    dp[0][i] = i

for k in range(1, 15):
    for n in range(1, 15):
        dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

for i in range(a):
    k = int(input())
    n = int(input())
    print(dp[k][n])








