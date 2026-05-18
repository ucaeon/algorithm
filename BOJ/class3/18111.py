import sys

INF = int(1e9)

n, m, b = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = [INF, -1]
for h in range(257):
    result_t = 0
    inven = b
    for i in range(n):
        for j in range(m):
            if graph[i][j] < h:
                result_t += h - graph[i][j]
                inven -= h - graph[i][j]
            elif graph[i][j] > h:
                result_t += 2 * (graph[i][j] - h)
                inven += graph[i][j] - h

    if inven >= 0 and result[0] >= result_t:
        result[0] = result_t
        result[1] = h

print(' '.join(map(str, result)))