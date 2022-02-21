from itertools import permutations
n = int(input())
arr = [i for i in range(1,n+1)]
for i in list(permutations(arr, n)):
    for j in i: # 리스트 하나를 꺼내서 요소 하나씩 공백을 넣어서 출력 
        print(j, end= ' ')
    print() # 줄바꿔서 모든 리스트 & 리스트 요소 출력 함
