import heapq

jobs = [[0, 3], [1, 9], [2, 6], [2, 3]]

answer = 0
heap = []
for job in jobs:
    heapq.heappush(heap, job)
for i in range(len(heap)):
    print(heapq.heappop(heap))