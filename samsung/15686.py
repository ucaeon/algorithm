from itertools import combinations

# 입력 받기 & 집, 치킨집 좌표 저장
n, m = map(int, input().split())

koko = []
home = []
min_value = float('inf')


for i in range(n):
    a = list(map(int, input().split()))

    for j in range(len(a)):
        if a[j]== 1:
            home.append((i, j))
        elif a[j] == 2:
            koko.append((i, j))
        else:
            continue

# 조합 만들기
for comb in combinations(koko, m):
    total = 0

    for hx, hy in home:
        min_dist = float('inf')

        for cx, cy in comb:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        total += min_dist
    
    if total < min_value:
        min_value = total

print(min_value)