# 트리
# 13116_30번

# import sys
# if __name__ == "__main__":
#     T = int(input())
#     for _ in range(T):
#         # 두 정수 입력받기
#         A, B = map(int, sys.stdin.readline().split())
        
#         listA = [] # 정수 A가 되기위해 거쳐온 꼭지점의 리스트
#         listB = [] # 정수 B가 되기위해 거쳐온 꼭지점의 리스트
#         while A > 1: # 정수 A가 1이 될 때까지 거쳐온 꼭지점 구하기
#             A //= 2 
#             listA.append(A)
#         while B > 1: # 정수 B가 1이 될 때까지 거쳐온 꼭지점 구하기
#             B //= 2
#             listB.append(B)

#         for i in listA: # 공통으로 포함되는 꼭지점 중 최대값 구하기
#             if i in listB:
#                 print(i*10)
#                 break            


import sys
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        # 두 정수 입력받기
        A, B = map(int, sys.stdin.readline().split())
        while True:
            if A > B:
                A //= 2
            elif A < B:
                B //= 2
            else:
                print(A*10)
                break 