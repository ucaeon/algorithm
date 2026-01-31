n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

result = []
stack = []
idx = 1
flag = False

for i in data:
    while idx <= i:
        stack.append(idx)
        idx += 1
        result.append('+')
    
    if i == stack[-1]:
        result.append('-')
        stack.pop()
    else:
        flag = True
        break
    
if flag:
    print('NO')
else:
    for i in result:
        print(i)

