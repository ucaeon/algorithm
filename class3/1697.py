from collections import deque

h, c = map(int, input().split())

queue = deque([h])
dist = [-1] * 100001
dist[h] = 0

while queue :
    x = queue.popleft()

    if x == c:
         print(dist[x])
         break

    gx = [x - 1, x + 1, 2 * x]

    for i in range(3):
        nx = gx[i]
        if 0 <= nx < 100001 and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            queue.append(nx)

            

