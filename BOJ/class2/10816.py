from collections import Counter

data = []
num = []

n = int(input())
data = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

data = Counter(data)
result = [0] * m

for i in range(m):
    if num[i] in data:
        result[i] += data[num[i]]

for i in result:
    print(i, end = ' ')