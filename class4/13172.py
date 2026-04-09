MOD = 1000000007

m = int(input())
sum = 0

for _ in range(m):
    a, b = map(int, input().split())

    # 역원 pow 쓰기
    a = pow(a, MOD - 2, MOD)
    sum = (sum + (a * b))

print(sum % MOD)