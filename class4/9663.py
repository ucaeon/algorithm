n = int(input())

visited = [False] * n
queen = [0] * n
num = 0

def backtrack(depth):
    global num

    if depth == n:
        num += 1
        return

    for i in range(n):      
        can_place = True

        for j in range(depth):  
            if queen[j] == i or abs(depth - j) == abs(i - queen[j]): 
                can_place = False
                break

        if can_place:
            queen[depth] = i
            backtrack(depth + 1)


backtrack(0)
print(num)