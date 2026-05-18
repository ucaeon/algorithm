from collections import deque

n = int(input())

for i in range(n):
    data = str(input())
    q = deque()
    result = True

    for i in data:
        if i == '(':
            q.append(i)
        elif i == ')' and '(' in q:
            q.pop()
        elif i == ')' and len(q) == 0:
            result = False
    
    if result and len(q) == 0:
        print('YES')
    else:
        print('NO')
        
    



