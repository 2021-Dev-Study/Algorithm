## 첫번째 풀이 딕셔너리로 풀어야하는거 생각해 냈는데 index함수 사용해서 시간 초과 ## 
import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

s_num = sorted(list(set(num))) # 처음에 num.sort() 했는데, 이러면 num값이 아예 정렬된 채로 변경돼서 sorted함수 사용 

dic = dict()
for i in range(len(s_num)):
    dic[s_num[i]] = s_num.index(s_num[i])  # index 사용해서 시간 초과. list.index(i)의 형태는 시간복잡도 O(N)
 

for i in num:
    print(dic[i] , end= ' ')


############# 재풀이 ############# 
import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

s_num = sorted(list(set(num))) # 두번째 예제 참고해서 중복값을 제거하기 위해 set함수를 사용하고 list로 바꿔준뒤 정렬

dic = dict() # 딕셔너리 생성

for i in range(len(s_num)): # 중복 제거한 원소 개수만큼 반복하여 딕셔너리에 key = value 값 저장 
    dic[s_num[i]] = i # key에 정렬된 리스트인 s_num의 원소를 넣고, 순서대로 정렬된 상태기 때문에 i값을 넣어줌   
    # 생각해보니 s_num은 정렬된 상태라 index함수를 사용할게 아니라 그냥 i로 넣어주면 됐었음..

#print(dic)  # {-10: 0, -9: 1, 2: 2, 4: 3}


for i in num:
    print(dic[i] , end= ' ') # num의 value 값을 출력 
