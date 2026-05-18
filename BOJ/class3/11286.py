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
            if heap[0][1] == 0: 
                result.append(-(heapq.heappop(heap)[0]))
            else:
                result.append(heapq.heappop(heap)[0])
    else:
        if a < 0:
            heapq.heappush(heap, (abs(a), 0))
        else:
            heapq.heappush(heap, (abs(a), 1))

for i in result:
    print(i)
