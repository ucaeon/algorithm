n = int(input())
data = []

for i in range(n):
    m = list(map(int, input()))
    data.append(m)

visited = [[False] * n for _ in range(n)]
r_house = []
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and data[i][j] == 1:
            count += 1
            stack = [(i, j)]            
            visited[i][j] = True
            house = 1

            while stack:
                y, x = stack.pop()

                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]

                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[ny][nx] and data[ny][nx] == 1:
                            house += 1
                            stack.append([ny, nx])
                            visited[ny][nx] = True
            r_house.append(house)

print(count)
result = sorted(r_house)
for i in result:
    print(i)
           

