dic = {}

n = int(input())
data = list(map(int, input().split()))
count = list(set(data))
count.sort()
num = 0

for i in count:
    dic[i] = num
    num += 1

for i in range(len(data)):
    data[i] = dic[data[i]]

print(' '.join(map(str, data)))