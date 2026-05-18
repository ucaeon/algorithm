from collections import deque

data = deque()

n = int(input())

for i in range(1, n + 1):
    data.append(i)

while len(data) > 1:
        data.popleft()
        data.append(data.popleft())

print(data[0])