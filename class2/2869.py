a, b, v = map(int, input().split())

f = v - a
d = a - b
c = f // d

if f % d == 0:
    print(c + 1)
else: 
    print(c + 2)