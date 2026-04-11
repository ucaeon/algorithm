# ??
row, col, goal = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]

time = 0
cal = ''
c_length = 3
r_length = 3

while True:
    new_data = []
    max_len = 0
    # 종료 조건
    if 0 <= row - 1 < r_length and 0 <= col - 1 < c_length:
        if data[row - 1][col - 1] == goal:
            print(time)
            break
    if time > 100:
        print(-1)
        break

    # 무슨 연산할지 파악
    if r_length >= c_length:
        cal = 'R'
    else:
        cal = 'C'

    # R 연산
    if cal == 'R':
        for i in range(r_length):
            cnt = {}
            nr = []     
            for j in data[i]:
                if j == 0:
                    continue
                if j in cnt:
                    cnt[j] += 1
                else:
                    cnt[j] = 1
            result = sorted(cnt.items(), key = lambda x : (x[1], x[0]))
            
            for num, cnt in result:
                nr.append(num)
                nr.append(cnt)

            nr = nr[:100]
            max_len = max(max_len, len(nr))
            new_data.append(nr)

        for i in range(len(new_data)):
            while len(new_data[i]) < max_len:
                new_data[i].append(0)
        data = new_data

    # C 연산
    if cal == 'C':
        data = list(map(list, zip(*data)))

        new_data = []
        max_len = 0

        for i in range(len(data)):
            cnt = {}
            nr = []

            for j in data[i]:
                if j == 0:
                    continue
                if j in cnt:
                    cnt[j] += 1
                else:
                    cnt[j] = 1

            result = sorted(cnt.items(), key=lambda x: (x[1], x[0]))

            for num, cnt_num in result:
                nr.append(num)
                nr.append(cnt_num)

            nr = nr[:100]
            max_len = max(max_len, len(nr))
            new_data.append(nr)

        for i in range(len(new_data)):
            while len(new_data[i]) < max_len:
                new_data[i].append(0)

        data = list(map(list, zip(*new_data)))

    r_length = len(data)
    c_length = len(data[0])
    time += 1






