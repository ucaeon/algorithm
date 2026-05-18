data = []
num = []

n = int(input())
data = set(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

for i in range(1, m + 1):
    if num[i - 1] in data:
        print(1)
    else:
        print(0)