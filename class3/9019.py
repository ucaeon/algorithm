from collections import deque

t = int(input())

result = []
for i in range(t):
    a, b = map(int, input().split())

    visited = [False] * 10000
    queue = deque([(a, '')])
    visited[a] = True

    while queue:
        k, path = queue.popleft()

        if k == b:
            result.append(path)
            break
        else:
            d = (k * 2) % 10000
            if not visited[d]:
                visited[d] = True
                queue.append((d, path + 'D'))

            s = 9999 if k == 0 else k - 1
            if not visited[s]:
                visited[s] = True
                queue.append((s, path + 'S'))

            l = (k % 1000) * 10 + (k // 1000)
            if not visited[l]:
                visited[l] = True
                queue.append((l, path + 'L'))

            r = (k % 10) * 1000 + (k // 10)
            if not visited[r]:
                visited[r] = True
                queue.append((r, path + 'R'))

for i in result:
    print(i)
            
            



