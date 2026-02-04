a, b =  map(int, input().split())

gcd = []

for i in range(a):
    for j in range(b):
        if a % (i + 1) == 0 and b % (j + 1) == 0 and i == j:
            gcd.append(i + 1)
            
print(max(gcd))
print((a * b) // max(gcd))
