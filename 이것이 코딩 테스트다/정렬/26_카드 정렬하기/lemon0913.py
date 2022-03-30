# import sys
# if __name__ == "__main__":
#     N = int(input())
#     cards = [0] * N
#     for i in range(N):
#         cards[i] = int(sys.stdin.readline())
    
#     cards.sort(reverse = True)

#     if N == 1:
#         print(0)
#     else:
#         result = []
#         s = cards.pop()
#         while cards:
#             s += cards.pop()
#             result.append(s)

#         print(sum(result))


# heap 자료 구조 활용 -> 이걸 안쓰면 매 연산마다 sort()연산을 해야해서 효율이 매우 안좋을 것 같음...
import heapq
import sys
if __name__ == "__main__":
    N = int(input())

    heap = []
    for i in range(N):
        heapq.heappush(heap, int(sys.stdin.readline()))
    
    s = 0
    while len(heap) != 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        s += x + y
        heapq.heappush(heap, x+y)
        
    print(s)




