from collections import deque

n, m = map(int, input().split())
tp = list(map(int, input().split()))
tp = tp[1:]

data = [[] for _ in range(n + 1)]
party = []

for i in range(m):
    a = list(map(int, input().split()))
    party.append(a[1:])
    for j in range(1, len(a)):
        for k in range(j, len(a)):
            if j == k: 
                continue
            data[a[j]].append(a[k])
            data[a[k]].append(a[j])

visited = [False] * (n + 1)
q = deque()

for i in tp:
    q.append(i)
    visited[i] = True

while q:
    a = q.popleft()

    for i in data[a]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

cnt = 0
for i in party:
    for j in i:
        if visited[j]:
            break
    else:
        cnt += 1

print(cnt)



