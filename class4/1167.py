n = int(input())

data = [[] for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] == -1:
            break
        else:
            if i % 2 != 0:
                data[a[0]].append((a[i], a[i + 1]))

max_dist = 0
end_node = 0

def tree(node, parent, dist):
    global max_dist, end_node

    if dist > max_dist:
        max_dist = dist
        end_node = node

    for en, d in data[node]:
        if parent == en:
            continue
        tree(en, node, dist + d)

tree(1, 0, 0)
max_dist = 0
tree(end_node, 0, 0)

print(max_dist)











    