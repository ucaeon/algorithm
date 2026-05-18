n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

path = []
visited = [False] * (n + 1)

def backtrack():
    if len(path) == m:
        print(*path)
        return
    
    prev = None

    for i in range(len(data)):
        if visited[i]:
            continue
        
        if data[i] == prev:
            continue

        path.append(data[i])
        prev = data[i]
        visited[i] = True


        backtrack()

        path.pop()
        visited[i] = False

backtrack()
