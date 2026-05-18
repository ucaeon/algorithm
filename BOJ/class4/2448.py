# 입력
n = int(input())
data = [[' '] * (2 * n - 1) for _ in range(n)]

def star(x, y, size):
    if size == 3:
        data[x][y] = '*'
        data[x + 1][y - 1] = '*'
        data[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            data[x + 2][y + i] = '*'
        return

    half = size // 2

    star(x, y, half)
    star(x + half, y - half, half)
    star(x + half, y + half, half)

star(0, n - 1, n)

for i in range(n):
    print(''.join(data[i]))