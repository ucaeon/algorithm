n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for day in range(n - 1, -1, -1):
    time, pay = schedule[day]

    if day + time <= n:
        dp[day] = max(dp[day + 1], pay + dp[day + time])
    else:
        dp[day] = dp[day + 1]

print(dp[0])
    