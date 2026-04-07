n, b = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 행렬 곱 계산
def matrix_mult(am, bm):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += am[i][k] * bm[k][j]
                result[i][j] %= 1000
    return result

# 분할 정복 함수
def power(data, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                data[i][j] = data[i][j] % 1000
        return data

    half = power(data, b // 2)

    if b % 2 == 0:
        return matrix_mult(half, half)
    else:
        return matrix_mult(matrix_mult(half, half), data)
    
ans = power(data, b)

for i in range(n):
    print(*ans[i])