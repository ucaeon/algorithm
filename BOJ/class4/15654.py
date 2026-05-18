n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

visited = [False] * (n + 1)
path = []

def backtrack():
    if len(path) == m:
        print(*path)
        return

    for i in range(len(data)):
        if visited[i]:
            continue

        visited[i] = True
        path.append(data[i])

        backtrack()

        path.pop()
        visited[i] = False

backtrack()