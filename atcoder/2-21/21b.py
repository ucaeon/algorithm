n, m = map(int, input().split())

gr = []
result = []

for i in range(n):
    data = []
    find = False

    l = int(input())
    data = list(map(int, input().split()))

    for i in range(len(data)):
        if not data[i] in gr:
            result.append(data[i])
            gr.append(data[i])
            find = True
            break
    if not find:
        result.append(0)

for i in result:
    print(i)

