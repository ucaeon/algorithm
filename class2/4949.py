from collections import deque

while True:
    data = str(input())

    q = deque()
    result = True

    if data == '.':
        break

    for i in data:
        if i == '(' or i == '[':
            q.append(i)
        elif i == ')' and len(q) > 0 and q[-1] == '(':
            q.pop()
        elif  i == ']'and len(q) > 0 and q[-1] == '[':
            q.pop()

        elif i == ')' or i == ']':
            result = False
            break
        
    if result and len(q) == 0:
        print('yes')
    else:
        print('no')