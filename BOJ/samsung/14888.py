n = int(input())
data = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_value = int(1e10)
max_value = -int(1e10)

def backtrack(depth, sum, plus, minus, mul, div):
    global min_value, max_value

    if depth == n:
        min_value = min(sum, min_value)
        max_value = max(sum, max_value)
        return
    
    num = data[depth]

    if plus > 0:
        backtrack(depth + 1, sum + num, plus - 1, minus, mul, div)

    if minus > 0:
        backtrack(depth + 1, sum - num, plus, minus - 1, mul, div)

    if mul > 0:
        backtrack(depth + 1, sum * num, plus, minus, mul - 1, div)

    if div > 0:
        if sum >= 0:
            backtrack(depth + 1, sum // num, plus, minus, mul, div - 1)
        else:
            backtrack(depth + 1, -(-sum // num), plus, minus, mul, div - 1)


backtrack(1, data[0], plus, minus, mul, div)


print(max_value)
print(min_value)

