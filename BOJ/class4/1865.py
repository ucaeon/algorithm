# 벨만포드
def bellman_ford(n, data):
    dist = [0] * (n + 1)

    # 작으면 갱신(음수 사이클 찾기)
    for i in range(n):
        for a, b, c in data:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                
                # n반복이 되면? 음수 사이클 존재
                if i == n - 1:
                    return True
    return False

tc = int(input())

result = []

for _ in range(tc):
    a, b, c = map(int, input().split())
    data = []

    # 도로 저장(무방향으로)
    for i in range(b):
        k = list(map(int, input().split()))
        data.append((k[0], k[1], k[2]))
        data.append((k[1], k[0], k[2]))

    # 웜홀 저장
    for i in range(c):
        k = list(map(int, input().split()))
        data.append((k[0], k[1], -k[2]))
    
    if bellman_ford(a, data):
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)

