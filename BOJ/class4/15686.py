n, m = map(int, input().split())
data = []
home = []
chickens = []

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            home.append((i, j))
        elif data[i][j] == 2:
            chickens.append((i, j))

answer = float('inf')

def backtrack(start, selected):
    global answer
    
    if len(selected) == m:
        total = 0

        for x, y in home:
            min_dist = float('inf')
            for cx, cy in selected:
                dist = abs(x - cx) + abs(y - cy)
                if dist < min_dist:
                    min_dist = dist

            total += min_dist

        if total < answer:
            answer = total
        return

    for i in range(start, len(chickens)):
        selected.append(chickens[i]) 
        backtrack(i + 1, selected)
        selected.pop()

backtrack(0, [])   

print(answer)