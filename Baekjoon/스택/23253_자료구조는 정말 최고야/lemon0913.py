# 스택 (실버 3까지)
# 23253_자료구조는 정말 최고야


# 예제로 돌렸을 때 답은 나옴...그치만 시간 초과
# import sys

# if __name__ == "__main__":
#     N, M = list(map(int, input().split()))
    
#     # 각 더미에 책이 몇 권인지, 어떻게 쌓여있는지 입력받기
#     dummy = []
#     count = []
#     for i in range (M):
#         count.append(int(sys.stdin.readline()))
#         dummy.append(list(map(int, sys.stdin.readline().split())))
    
#     # 각 더미의 제일 위에 찾는 번호가 있다면 더미에서 꺼내기
#     for book_num in range(1, N+1):
#         for dummy_num in range(M):
#             while dummy[dummy_num]:
#                 if dummy[dummy_num][-1] == book_num:
#                     dummy[dummy_num].pop()
#                 else:
#                     break

        
#     #모든 더미가 비어있으면 올바른 순서대로 모든 교과서를 꺼낸것임
#     sum = 0
#     for i in range(M):
#         sum += len(dummy[i])
    
#     if sum == 0:
#         print("Yes")
#     else:
#         print("No")




# 풀이 2
# 그냥 모든 더미가 내림차순으로 정렬되어 있기만 하면 됨
# 답은 맞는데 문제는 이건 스택을 사용 안함...
import sys

       

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    
    b = True

    # 각 더미를 입력받고 각각이 내림차순인지 확인하기
    for i in range (M):
        num = int(sys.stdin.readline())
        dummy = list(map(int, sys.stdin.readline().split()))

        for j in range (num-1):
            if dummy[j] < dummy[j+1]: # 해당 더미가 내림차순이 아니면 확인 그만 두기
                b = False
                break
       

    
    if b == True:
        print("Yes")
    else:
        print("No")

