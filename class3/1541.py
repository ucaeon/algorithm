data = list(map(str, input().split('-')))

result = 0
total = []

for i in range(len(data)):
    n = list(map(int, data[i].split('+')))
    total.append(sum(n))

result = total[0]

for i in range(1, len(total)):
    result -= total[i]

print(result)