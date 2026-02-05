n = int(input())
count = 0

x = n // 5 

while x >= 0:
    if (n - (5 * x)) % 3 == 0:
        count = x + ((n - (5 * x)) // 3)
        print(count)
        break
    else:
        x -= 1
        continue
else:
    print(-1)