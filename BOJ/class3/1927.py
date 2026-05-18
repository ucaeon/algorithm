import heapq

n = int(input())

heap = []
result = []

for i in range(n):
    a = int(input())
    if a == 0:
        if not heap:
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)

for i in result:     
    print(i)