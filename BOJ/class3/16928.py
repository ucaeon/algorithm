from collections import deque

n, m = map(int, input().split())

data = [0] * 101
for i in range(n + m):
    x, y = map(int, input().split())
    data[x] = y

visited = [-1] * 101
visited[1] = 0
queue = deque()
queue.append((1))

while queue:
    a = queue.popleft()

    if a == 100:
        print(visited[a])
        break
    else:
        for i in range(1, 7):
            na = a + i

            if na <= 100:
                if data[na] != 0:
                    next = data[na]
                else: 
                    next = na

                if visited[next] == -1:
                    visited[next] = visited[a] + 1
                    queue.append(next)
                
    
