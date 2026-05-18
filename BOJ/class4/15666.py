n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

path = []

def backtrack(start):
    if len(path) == m:
        print(*path)
        return
    
    prev = None
    for i in range(start, n):
        if prev == data[i]:
            continue
    
        path.append(data[i])
        prev = data[i]

        backtrack(i)

        path.pop()

backtrack(0)