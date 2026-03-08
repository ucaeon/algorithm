n, m = map(int, input().split())

path = []

def backtrack(start):
    if len(path) == m:
        print(*path)
        return
    
    for i in range(start, n + 1):
        path.append(i)
        backtrack(i)
        path.pop()
        
backtrack(1)
