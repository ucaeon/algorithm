from collections import deque

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    data = list(map(int, input().split()))

    q = deque()

    for i in range(len(data)):
        q.append((i, data[i]))

    count = 0

    while q:
        i, j = q.popleft()
        
        if len(q) > 0 and j < max(j for _, j in q):
            q.append((i, j))
        else:
            count += 1

            if i == b:
                print(count)
                break

            
            

                






   
    
            
    
