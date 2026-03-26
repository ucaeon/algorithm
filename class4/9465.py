t = int(input())

for _ in range(t):
    n = int(input())

    data = []
    for _ in range(2):
        data.append(list(map(int, input().split())))

    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = data[0][0]
    dp[0][2] = data[1][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + data[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + data[1][i]

    print(max(dp[-1]))