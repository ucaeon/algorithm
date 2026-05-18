n, m = map(int, input().split())

money = []
count = 0
target = m

for i in range(n):
    money.append(int(input()))

money = sorted(money, reverse = True)

for i in money:
    if target > 0:
        if (target // i) > 0:
            count += (target // i)
            target = (target % i)
        else:
            continue

print(count)