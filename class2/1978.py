n = int(input())
data = list(map(int, input().split()))

count = 0

for i in data:
    result = True
    if i == 1:
            result = False

    for j in range(2, i - 1):
        if i % j != 0:
            continue
        else:
            result = False

    if result:
        count += 1

print(count)


            

    