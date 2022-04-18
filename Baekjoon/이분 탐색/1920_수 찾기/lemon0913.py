# 이분 탐색으로 풀기
# if __name__ == "__main__":
#     N = int(input())
#     list1 = list(map(int, input().split()))
#     list1.sort() # 이분 탐색을 위해 리스트 정렬하기
#     M = int(input())
#     list2 = list(map(int, input().split()))


#     # 이분 탐색을 수행하는 함수
#     def binary(lst, target, start, end):

#         while start <= end:
#             mid = (start+end)//2

#             if lst[mid] == target:
#                 return 1
#             elif lst[mid] > target:
#                 end = mid-1
#             else:
#                 start = mid+1
        
#         return 0
    
#     for i in list2:
#         print(binary(list1, i, 0, N-1))

# set()으로 풀기
# 그냥 단순하게 리스트내에 값이 존재하나를 확인한다면 set 자료형 사용하기
if __name__ == "__main__":
    N = int(input())
    list1 = list(map(int, input().split()))
    list1 = set(list1) # 리스트1을 set 자료형으로 바꾸기
    M = int(input())
    list2 = list(map(int, input().split()))

    for i in list2:
        if i in list1:
            print(1)
        else:
            print(0)   


