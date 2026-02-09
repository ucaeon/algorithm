n, m = map(int, input().split())
data = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        stack = [i]

        while stack:
            a = stack.pop()
            if not visited[a]:
                visited[a] = True
                
                for j in data[a]:
                    if not visited[j]:
                        stack.append(j)
print(count)
