n = int(input())
result = []

for i in range(n):
    s = str(i)
    l = list(s)
    num = 0

    for j in l:
        num += int(j)
    
    if (int(s) + num) == n:
        result.append(i)
    else:
        continue

if len(result) == 0:
    print(0) 
else:
    print(result[0])

    