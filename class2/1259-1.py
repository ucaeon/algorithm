while True:
    data = list(map(int, input()))

    if data == [0]:
        break

    result = 'yes'

    for i in range(len(data) // 2):
        if data[i] == data[(len(data) -1) - i]:
            continue
        else:
            result = 'no'
    
    print(result)