from collections import deque

t = int(input())

for i in range(t):
    p = list(map(str, input()))
    n = int(input())
    reversed = False
    error = False

    if n == 0:
        c = input()
        data = deque([])
    else:
        data = list(map(int, input()[1:-1].split(',')))
        data = deque(data)
    
    for j in p:
        if j == 'R':
            reversed = not reversed
        else:
            if len(data) == 0:
                error = True
                break
            
            if not reversed:
                data.popleft()
            else:
                data.pop()

    if error:
        print('error')
    else:
        if reversed:
            data.reverse()
        
        print('[' + ','.join(map(str, data)) + ']')
    

