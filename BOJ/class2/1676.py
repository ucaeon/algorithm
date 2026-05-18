n = int(input())

data = 1
count = 0

for i in range(1, n + 1):
    data *= i

data = list(map(int, str(data)))
data.reverse()

for i in range(len(data)):
    if data[i] == 0:
        count += 1
    else:
        break
    

print(count)