while True:
    data = []
    data = list(map(int, input().split()))
    if data.count(0) == 3:
        break

    else:
        data.sort()
        if data[0]**2 + data[1]**2 == data[2]**2:
            print('right')
        else:
            print('wrong')