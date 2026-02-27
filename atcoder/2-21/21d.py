n = int(input())
data = list(map(int, input().split()))

dic = {}
count = 0

for x in data:
    if x - 1 in dic:
        dic[x] = dic[x - 1] + 1
    else:
        dic[x] = 1

print(max(dic.values()))