n = int(input())

data = []
count = 0

for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

data.sort(key = lambda x : (x[1], x[0]))

end = 0

for i in data:
    if end <= i[0]:
        print(i)
        count += 1
        end = i[1]
    else:
        continue
print(count)
