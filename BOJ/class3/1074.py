n, r, c = map(int, input().split())

size = 2 ** n
result = 0

while size > 1:
    half = size // 2

    if r < half and c < half:     
        q = 0
    elif r < half and c >= half:      
        q = 1
        c -= half
    elif r >= half and c < half:     
        q = 2
        r -= half
    else:                        
        q = 3
        r -= half
        c -= half

    result += q * (half * half)
    size = half

print(result)