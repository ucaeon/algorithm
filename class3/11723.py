import sys

n = int(input())
s = set()

for i in range(n):
    data = list(map(str, input().split()))

    if len(data) == 1:
        a = data[0]
        if a == 'all':
            s = set([i for i in range(1, 21)])
        elif a == 'empty':
            s.clear()

    else:
        a, b = data[0], int(data[1])

        if a == 'add':
            s.add(b)
        elif a == 'remove':
            s.discard(b)
        elif a == 'check':
            if b in s:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if b in s:
                s.discard(b)
            else:
                s.add(b)
        
        