n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

visited = [False] * n
min_abs = 100000000

def backtrack(start, depth):
    global min_abs

    if depth == n // 2:
        # 팀 나누기
        start_team = []
        link_team = []

        for i in range(n):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        # 점수 계산
        start_score = 0
        link_score = 0

        for i in range(len(start_team)):
            for j in range(i + 1, len(start_team)):
                a = start_team[i]
                b = start_team[j]
                start_score += (data[a][b] + data[b][a])

        for i in range(len(link_team)):
            for j in range(i + 1, len(link_team)):
                a = link_team[i]
                b = link_team[j]
                link_score += (data[a][b] + data[b][a])

        min_abs = min(min_abs, abs(start_score - link_score))
        return

    for i in range(start, n):
        visited[i] = True
        backtrack(i + 1, depth + 1)
        visited[i] = False


backtrack(0, 0)
print(min_abs)


     
