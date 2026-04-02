data = list(map(str, input()))
boom = input()

stack = []

for i in range(len(data)):
    stack.append(data[i])
    temp = []

    if len(stack) >= len(boom):
        for i in range(len(boom)):
            temp.append(stack[-len(boom) + i])

        if temp == list(boom):
            for _ in range(len(boom)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')