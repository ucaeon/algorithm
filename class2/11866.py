from collections import deque

n, k = map(int, input().split())
q = deque()
result = []

for i in range(1, n + 1):
    q.append(i)

for i in range(n):
    if len(q) > 0:
        q.rotate(-(k-1))
        result.append(q.popleft())

print("<" + ", ".join(map(str, result)) + ">")
