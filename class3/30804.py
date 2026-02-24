n = int(input())
data = list(map(int, input().split()))

start = 0
end = 0
result = 0
dic = {}

while end < n:
    if not data[end] in dic:
        dic[data[end]] = 1
    else:
        dic[data[end]] += 1

    while len(dic) > 2:
        dic[data[start]] -= 1
        if dic[data[start]] == 0:
            del dic[data[start]]
        start += 1
    
    result = max(result, end - start + 1)
    end += 1

print(result)


