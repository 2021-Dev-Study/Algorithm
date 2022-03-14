# 단계별 - 그리디 알고리즘
# 13305_주유소

# 부분성공..??58점..?????
# 가장 적은 비용으로 주유할 수 있는 곳에서 최대한 주유하기
# from collections import deque
# if __name__ == "__main__":
#     N = int(input())
#     roads = deque(list(map(int, input().split())))
#     money = deque(list(map(int, input().split())))

#     money.pop() # 맨 마지막에 도착한 도시의 기름값은 버리기
#     result = 0
#     while roads:
#         m = min(money) # 기름값의 최소값 구하기
#         idx = money.index(m) # 그 최소값의 인덱스 구하기
#         cnt = 0
#         for i in range(len(money)-idx): # 기름값이 최소인 곳 이후의 거리 구하기 
#             cnt += roads.pop()
#             money.pop()
#         result += cnt*m # 최소 기름 값 * 이후 거리
#     print(result)



# 이전에 주유한 기름값보다 지금 기름값이 더 싸다면 주유하기
if __name__ == "__main__":
    N = int(input())
    roads = list(map(int, input().split()))
    money = list(map(int, input().split()))

    result = roads[0] * money[0]
    tmp = money[0]
    for i in range(1, len(roads)):
        if tmp > money[i]:
            result += roads[i]*money[i]
            tmp = money[i]
        else:
            result += roads[i] * tmp
    print(result)