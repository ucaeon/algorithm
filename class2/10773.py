data = []
result = []
num = 0

n = int(input())
for i in range(n):
    data.append(int(input()))

for i in data:
    if i != 0:
        result.append(i)
    elif i == 0 and len(result) > 0:
        result.pop()

for i in result:
    num += i
print(num)
