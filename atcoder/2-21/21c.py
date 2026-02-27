from collections import deque

t = int(input())
result = []

for i in range(t):
    n, m = map(int, input().split())
    A = deque(list(map(int, input().split())))
    B = list(map(int, input().split()))
    mon = deque()
    day = deque()
    sun = 0
    count = 0

    for j in range(n):
        sun += 1
        mon.append(A[j])
        day.append(sun)

        while B[j] > 0:
            if mon[0] > B[j]:
                mon[0] -= B[j]
                B[j] = 0
            else:
                B[j] -= mon[0]
                mon.popleft()
                day.popleft()

        while mon and sun - day[0] >= m:
            mon.popleft()
            day.popleft()

    count = sum(mon)
    result.append(count)

for i in result:
    print(i)