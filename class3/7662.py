import heapq


t = int(input())

for i in range(t):
    n = int(input())
    heap_min = []
    heap_max = []
    dic = {}

    for j in range(n):
        a, b = input().split()
        b = int(b)
        
        if a == 'I':
            heapq.heappush(heap_max, -b)
            heapq.heappush(heap_min, b)
            dic[b] = dic.get(b, 0) + 1

        else: 
            while heap_min and b == -1:
                x = heapq.heappop(heap_min)
                if dic[x] > 0:
                    dic[x] -= 1
                    break
            while heap_max and b == 1:
                x = -heapq.heappop(heap_max)
                if dic[x] > 0:
                    dic[x] -= 1
                    break

    while heap_min and dic.get(heap_min[0], 0) == 0:
        heapq.heappop(heap_min)
    while heap_max and dic.get(-heap_max[0], 0) == 0:
        heapq.heappop(heap_max)

    if not heap_min:
        print('EMPTY')
    else:
        print(-heap_max[0], heap_min[0])        
