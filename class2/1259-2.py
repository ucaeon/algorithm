from collections import deque

while True:
    data = deque(list(map(int, input())))

    if data[0] == 0:
        break

    result = 'yes'

    while (len(data) >= 2):
        a = data.popleft()
        b = data.pop()

        if a != b:
            result = 'no'

    print(result)

        