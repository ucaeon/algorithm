n = int(input())
result = [0] * 10001

for i in range(n):
    x = int(input())
    result[x] += 1


for i in range(len(result)):
    for j in range(result[i]):
        print(i)