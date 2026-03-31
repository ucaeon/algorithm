# 입력받고 dp 만들기
data1 = list(map(str, input()))
data2 = list(map(str, input()))

dp = [[0] * (len(data2) + 1) for _ in range(len(data1) + 1)]

# 비교하고 최적값 dp에 넣기
for i in range(1, len(data1) + 1):
    for j in range(1, len(data2) + 1):
        if data1[i - 1] == data2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(data1)][len(data2)])