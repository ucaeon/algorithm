n, m = map(int, input().split())
data = list(map(int, input().split()))

result = []

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        for z in range(j + 1, len(data)):
            total = data[i] + data[j] + data[z]

            if total > m:
                continue
            else:
                result.append(total)

print(max(result))