n, target = map(int, input().split())
data = list(map(int, input().split()))

start = 1
end = max(data)
result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in data:
        if i >= mid:
            count += (i - mid)

    if count >= target:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)