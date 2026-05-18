n = int(input())
m = int(input())
data = list(map(str, input()))

start = 0
end = 1
count = 0
k = 0

while end < m - 1:
    if data[end - 1] == 'I' and data[end] == 'O' and data[end + 1] == 'I':
        k += 1
        if k >= n:
            count += 1
        end += 2
    else:
        k = 0
        end += 1

print(count)
