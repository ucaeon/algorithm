data = []

n = int(input())

for i in range(n):
    data.append(int(input()))

if len(data) == 0:
    print(0)
else:
    data.sort()
    num = int(len(data) * (0.15) + 0.5)
    if len(data) == 1:
        print(data[0])
    else:
        data = data[num : -num] 
        print(int(sum(data) / len(data) + 0.5))
