n = int(input())

floor = 1
end = 1

while n > end:
    end += (6 * floor)
    floor += 1

print(floor)