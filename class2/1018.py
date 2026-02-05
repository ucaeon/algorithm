h, w = map(int, input().split())
data = []
result = []

for i in range(h):
    data.append(list(input()))

for x in range(h - 7):
    for y in range(w - 7): 
        countW = 0
        countB = 0

        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if data[i][j] != 'W':
                        countW += 1
                    if data[i][j] != 'B':
                        countB += 1
                else:
                    if data[i][j] != 'B':
                        countW += 1
                    if data[i][j] != 'W':
                        countB += 1

        result.append(min(countW, countB))

print(min(result))