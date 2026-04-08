tc = int(input())

result = []

for _ in range(tc):
    a, b, c = map(int, input().split())
    data = []

    for i in range(b):
        k = list(map(int, input().split()))
        data.append((k[0], k[1], k[2]))
        data.append((k[1], k[0], k[2]))

    for i in range(c):
        k = list(map(int, input().split()))
        data.append((k[0], k[1], -k[2]))

    def bellman_ford(n, data):
        dist = [0] * (n + 1)

        for i in range(n):
            for a, b, c in data:
                if dist[b] > dist[a] + c:
                    dist[b] = dist[a] + c

                    if i == n - 1:
                        return True
        return False
    
    if bellman_ford(a, data):
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)

