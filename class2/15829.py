n = int(input())
data = list(str(input()))
asc = []
value = 0

for i in data:
    asc.append(ord(i) - 96)

for i in range(n):
    value += asc[i] * (31 ** i)

print(value % 1234567891)
