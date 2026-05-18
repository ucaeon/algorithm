# 입력
n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * (2 * n)
down = n - 1
up = 0
seq = 0

while True:
    seq += 1

    # 벨트 & 로봇 회전
    down = (down + (2 * n - 1)) % (2 * n)
    up = (up + (2 * n - 1)) % (2 * n)

    if robot[down] == 1:
        robot[down] = 0

    # 로봇 이동
    for i in range(n - 1):
        now = (down - 1 - i) % (2 * n)
        next = (now + 1) % (2 * n)
        if robot[now] == 1 and robot[next] == 0:
            if belt[next] >= 1:
                robot[next] = 1
                robot[now] = 0
                belt[next] -= 1
                if robot[down] == 1:
                    robot[down] = 0
                
    # 로봇 올리기
    if robot[up] == 0 and belt[up] >= 1:
        robot[up] = 1
        belt[up] -= 1
    
    # 내구도 확인 및 종료
    if belt.count(0) >= k:
        break

print(seq)
        





