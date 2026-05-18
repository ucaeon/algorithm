n = int(input())

data = []
result = []
count = 1

for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue

        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    result.append(count)

for i in result:   
    print(i, end = ' ')
    


    