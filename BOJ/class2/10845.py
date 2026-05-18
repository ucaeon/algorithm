from collections import deque

n = int(input())

data = []
q = deque()

for i in range(n):
    data = input().split()

    if data[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else: 
            print(-1)

    if data[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else: 
            print(-1)
    
    if data[0] == 'empty':
        if len(q) == 0:
            print(1)
        else: 
            print(0)

    if data[0] == 'size':
        print(len(q))
    
    if data[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
            
    if data[0] == 'push':
        q.append(data[1])
    