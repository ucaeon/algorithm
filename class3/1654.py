n, target = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

start = 1
end = max(data)
result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in data:
        count += i // mid

    if count >= target:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)
