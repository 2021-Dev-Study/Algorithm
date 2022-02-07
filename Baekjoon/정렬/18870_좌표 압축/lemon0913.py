# 정렬 (단계별)
# 18870_좌표 압축

# if __name__ == "__main__":
#     N = int(input())
#     lst = list(map(int, input().split()))
#     sorted_lst = sorted(lst) # 오름차순으로 정렬한 리스트
    
#     zip = [] # 압축 좌표를 저장할 리스트
#     for i in range(N):
#         zip.append(sorted_lst.index(lst[i]))
        
#     print(" ".join(map(str, zip)))

# # 2 4 -10 4 -9
# # -10 -9 2 4 4



# 시간초과 문제 발생
# 찾아보니 lst.index(x) 때문이라고 -> O(N)
# 그래서 dictionary를 사용함 -> O(1)

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    sorted_lst = sorted(list(set(lst))) # 중복 제거후 오름차순으로 정렬한 리스트

    # 딕셔너리 자료형에 sorted_lst의 요소값 : 요소값의 인덱스 형태로 저장
    dic = {sorted_lst[i] : i for i in range(len(sorted_lst))} 

    for i in lst:
        print(dic[i], end=' ')

# 2 4 -10 4 -9
# -10 -9 2 4