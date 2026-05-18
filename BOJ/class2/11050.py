import math

a, b = map(int, input().split())
result = math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

print(result)