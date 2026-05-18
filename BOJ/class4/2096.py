n = int(input())

a, b, c = map(int, input().split())

max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    max0, max1, max2 = max_dp
    min0, min1, min2 = min_dp

    max_dp[0] = max(max0, max1) + a
    max_dp[1] = max(max0, max1, max2) + b
    max_dp[2] = max(max1, max2) + c

    min_dp[0] = min(min0, min1) + a
    min_dp[1] = min(min0, min1, min2) + b
    min_dp[2] = min(min1, min2) + c

print(max(max_dp), min(min_dp))