n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0
count = 0

for i in data:
    result = result + i
    count += result
print(count)