n = int(input())


for i in range(n):
    num = int(input())
    data = {}
    for j in range(num):
        a, b = map(str, input().split())
        if b in data:
            data[b] += 1
        else:
            data[b] = 1

    result = []
    total = 1
    for z in data.values():
        result.append(z + 1)
    
    for k in result:
        total *= k
    print(total - 1)
    