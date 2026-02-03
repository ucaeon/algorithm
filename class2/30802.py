n = int(input())
s = list(map(int, input().split()))
t, p = map(int, input().split())
count = 0

for i in s:
    if i % t > 0:
        count += (i // t) + 1
    else:
        count += (i // t)

a = n // p
b = n % p

print(count)
print(a, b)