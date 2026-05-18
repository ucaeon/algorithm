n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_start, b_start = 0, 0
result = []

while True:
    best = -1
    best_a = -1
    best_b = -1

    for i in range(a_start, n):
        for j in range(b_start, m):
            if a[i] == b[j]:
                if a[i] > best:
                    best = a[i]
                    best_a = i
                    best_b = j
                    
    if best == -1:
        break

    result.append(best)
    a_start = best_a + 1
    b_start = best_b + 1

print(len(result))
if result:
    print(*result)