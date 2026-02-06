n = int(input())
step = []
result = [0] * n

for i in range(n):
    step.append(int(input()))

if n == 1:
    print(step[0])
else:
    result[0] = step[0]
    result[1] = step[0] + step[1]
    
    for i in range(2, n):
        result[i] = max(result[i - 2] + step[i], result[i - 3] + step[i - 1] + step[i])

    print(result[-1])


