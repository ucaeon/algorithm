data = []
result = []
num = 1
max_num = 1
value = []

n = int(input())
for i in range(n):
    data.append(int(input()))

if n == 1:
    print(data[0])
    print(data[0])
    print(data[0])
    print(0)
else:
    if (sum(data) / n) < 0:
        result.append(int((sum(data) / n) - 0.5))
    else:
        result.append(int((sum(data) / n) + 0.5))

    data = sorted(data)
    result.append(data[n // 2])

    for i in range(1, n):
        if data[i] == data[i - 1]:
            num += 1
        else:
            num = 1
        
        if num > max_num:
            max_num = num
            value = [data[i - 1]]
        elif num == max_num:
            value.append(data[i - 1])
        
    if len(value) > 1:
        result.append(value[1])
    elif len(value) == 1:
        result.append(value[0])

    result.append(data[-1] - data[0])

for i in result:
    print(i)
