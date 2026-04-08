r, c = map(int, input().split())
data = [list(map(str, input())) for _ in range(r)]

visited = [False] * 26
start = ord(data[0][0]) - ord('A')
visited[start] = True
ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            idx = ord(data[nx][ny]) - ord('A')

            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, cnt + 1)
                visited[idx] = False

dfs(0, 0, 1)
print(ans)