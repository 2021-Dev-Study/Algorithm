import sys
N , M = map(int, sys.stdin.readline().split())
n_set = set() 
for _ in range(N):
    n_set.add(sys.stdin.readline().rstrip())

m_set = set()
for _ in range(M):
    m_set.add(sys.stdin.readline().rstrip())

result = sorted(list(n_set & m_set)) # 교집합 인것들을 list로 변환 후 정렬


print(len(result)) # 길이 출력 (듣과 보의 겹치는 것의 개수)
for i in result:
    print(i) # 겹치는 원소 출력 




########### 문제 잘못 이해.. 겹치는 값과 각 단어가 나온 횟수를 구하는 방법인줄.. ###########
# import sys
# N , M = map(int, sys.stdin.readline().split())
# arr = [0] * (N+M)
# for i in range(N+M):
#     arr[i] = sys.stdin.readline().rstrip()

# dic = dict()
# for i in arr:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# print("dic : ", dic)
# mid = 0
        
# arr1 = list(set(arr))
# arr1.sort()

# for i in arr1:
#     if dic[i] > mid:
#         mid = dic[i]
# print("mid : ", mid)

# print(mid)
# for i in arr1:
#     if dic[i] == mid:
#         print(i)
