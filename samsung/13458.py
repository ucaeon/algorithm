n = int(input())
data = list(map(int, input().split()))
n_data = []
b, c = map(int, input().split())
count = n

for i in range(len(data)):
    if data[i] - b <= 0:
        continue
    else:
        n_data.append(data[i] - b)

for i in range(len(n_data)):
    if n_data[i] == 0:
        continue
    elif (n_data[i] % c) != 0:
        count += (n_data[i] // c) + 1
    else: 
        count += (n_data[i] // c)
print(count)