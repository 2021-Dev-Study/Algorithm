S = input().upper() # 입력받고, 대문자로 바꿔줌
sarray = list(set(S)) # 일단 중복값 제거
array = []

for s in sarray:
    array.append(S.count(s)) # 문자열 S에서 s의 개수를 array에 추가 
mc = max(array) # 배열 array에서 max값  count(개수) 구하기 
if array.count(mc) != 1: # max count의 개수가 1이 아니면 max값이 더 있다는 것  
    print("?")
else:
    mi = array.index(mc) # max값개수가 1이면 array배열에서 max값이 있는 index찾아서 mi에 저장 max index
    print(sarray[mi]) # array 인덱스와 sarray가 같기 때문에 max값 인덱스번째 값을 찾음 


# 처음 생각했던 방법인데, 중복값 제거를 못해서 헤맸음
#S = input()
#array = []
#S = S.upper() # 대문자로 바꿔줌
#for i in range(len(S)):    
#    array.append(S.count(S[i]))
#    print("array : ",array)
#    mc = max(array)
#    print("mc : ",mc)
#    if array.count(mc) != 1:
#        print("?")
#    else:
#        mi = array.index(mc)
#        print(S[mi])    