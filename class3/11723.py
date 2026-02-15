import sys

input = sys.stdin.readline
n = int(input())
s = set()

for i in range(n):
    data = input().split()

    if len(data) == 1:
        a = data[0]
        if a == 'all':
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
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
        
        