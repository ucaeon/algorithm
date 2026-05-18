n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

white = 0
blue = 0

stack = []
stack.append((0, 0, n)) 

while stack:
    y, x, size = stack.pop()

    first = data[y][x]
    same = True

    for i in range(y, y + size):
        for j in range(x, x + size):
            if data[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        if first == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size // 2
        stack.append((y, x, half))     
        stack.append((y, x + half, half))         
        stack.append((y + half, x, half))       
        stack.append((y + half, x + half, half))  

print(white)
print(blue)