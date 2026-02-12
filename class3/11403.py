from collections import deque

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

result = [[0] * n for _ in range(n)]

for i in range(n):
    visited = [False] * n
    queue = deque()
    queue.append(i)

    while queue:
        a = queue.popleft()

        for j in range(n):
            if data[a][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = True
                result[i][j] = 1

for i in range(n):    
    for j in range(n):      
        print(result[i][j], end = ' ')
    print()

    



