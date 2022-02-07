import sys
N = int(sys.stdin.readline().rstrip())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
 
print(round(sum(num)/len(num))) # 산술 평균 
    
num.sort()
print(num[len(num)//2]) # 중앙값 , N은 무조건 홀수라는 조건이 있음 

# 최빈값 Counter 사용 
from collections import Counter
counter = Counter(num).most_common()
# print("counter", counter) # counter [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)] // 원소는오름차순 & 빈도는 내림차순으로 정렬됨  
if len(counter) > 1: # num 이 1개 이상이라면 
    if counter[0][1] == counter[1][1]: # Counter의 결과가 빈도가 가장 큰 것부터 나오므로 첫번째와 두번째를 비교했을 때 같다면 두번째결과를 출력함. Counter의 결과가(두번째로 작은 숫자, 최빈값) 이므로
        print(counter[1][0])
    else: # Counter의 결과에서 첫번째와 두번째를 비교했을때 같지 않다면, 첫번째 결과값이 최빈값이 되므로 첫번째 값을 출력 
        print(counter[0][0])
else:
    print(counter[0][0]) # num의 원소가 1개라면 첫번째 값을 출력 


### 최빈값 실패. Counter 가 아닌 count()이용 
# counter = []
# count = []
# for i in range(len(num)):
#     counter.append(num.count(num[i]))
# print("conter : ", counter)
# mc = max(counter)
# print("mc 카운트 : ", counter.count(mc))
# if counter.count(mc) != 1 :
#     for i in range(len(counter)):
#         if counter[i] != mc :
#            counter.pop(i)
#         mi = counter.index(mc)
#         count.append(num[mi])
#         print("count : ", count)
#     count.sort()
#     print(count[1])

# else :
#     mi = counter.index(mc)
#     print(num[mi])     
    
print(num[-1] - num[0])  # 범위  // 이미 정렬이 되어 있으므로 인덱스로 빼줌 