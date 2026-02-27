a = list(map(str, input()))
result = chr(ord(a[0]) + 32)

data = result

for i in range(len(a)):
    if i > 0:
        data += a[i]

print('Of' + data)