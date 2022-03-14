# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 06_무지의 먹방 라이브

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################

# 일부 런타임 에러 발생
def solution(food_times, k):
    var = len(food_times)
    foods = [i for i in range(var)]
    i = 0

    for now in range(k):
        if var==0:
            return -1
        
        food_times[foods[i]] -= 1
        if food_times[foods[i]] == 0:
            var -= 1
            del foods[i]
            i -= 1

        i = (i+1)%var
    
    return foods[i] + 1

""" Basic Solution
# ??? 아직 우선순위 큐를 제대로 활용+이해 하지 못한듯??
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, food_times[i], i+1)
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key =lambda x: x:[1])
    return result[(k - sum_value) % length]
"""


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5

    print(solution(food_times, k))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""