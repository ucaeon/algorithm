n = int(input())
data = list(map(int, input().split()))

max_score = 0
result = 0

for i in data:
    if max_score < i:
        max_score = i

for i in data:
    result += (i / max_score * 100)

result = result / n

print(result)
