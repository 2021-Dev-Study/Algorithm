# def getShortestDistance(weak):
#     shorted_distance = []

    
#     for i in range(len(weak)):
#         count = 0
#         current = weak[i]
#         prev = weak[i-1]
#         while current != prev:
#             prev = (prev + 1) % 12
#             count += 1
#         shorted_distance.append(count)
#     shorted_distance.sort(reverse=True)
#     return sum(shorted_distance[1:])

# def solution(n, weak, dist):
#     covered_distance = getShortestDistance(weak)
#     answer = 0
#     print(covered_distance)
#     while dist:
#         if covered_distance <= 0:
#             break
        
#         num = dist.pop()
#         covered_distance -= num
#         answer += 1
    
#     if answer == 0: answer = -1

#     return answer