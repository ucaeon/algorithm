import sys
sys.setrecursionlimit(10**5)

n = int(input())

data = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

max_dist = 0
end_node = 0

def tree(node, parent, dist):
    global max_dist, end_node

    if dist > max_dist:
        max_dist = dist
        end_node = node

    for en, d in data[node]:
        if en == parent:
            continue
        tree(en, node, dist + d)
    return 

tree(1, 0, 0)
max_dist = 0
tree(end_node, 0, 0)
print(max_dist)