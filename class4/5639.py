import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

data = []
while True:
    try:
        x = int(input())
        data.append(x)
    except:
        break


def solution(data):
    if len(data) == 0:
        return

    left = []
    right = []
    mid = data[0]
    for i in range(1, len(data)):
        if data[i] > mid:
            left = data[1:i]
            right = data[i:]
            break
    else:
        left = data[1:]
    
    solution(left)
    solution(right)
    print(mid)

solution(data)