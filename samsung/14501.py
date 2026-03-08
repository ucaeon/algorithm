from collections import deque

n = int(input())
data = deque()
total = 0

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

while data:
    print(data)
    a, b = data.popleft()

    if (len(data) + 1) - a < 0:
        break
    else:
        total += b
        for i in range(a - 1):
            data.popleft()
        
    