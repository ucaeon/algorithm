n, m = map(int, input().split())

num_data = {}
name_data = {}
result = []

for i in range(1, n + 1):
    name = input()

    num_data[i] = name
    name_data[name] = i

for i in range(m):
    a = input()

    if a.isdigit():
        result.append(num_data[int(a)])
    else:
        result.append(name_data[a])

for i in result:
    print(i)
