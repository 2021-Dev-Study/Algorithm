import sys
N = int(sys.stdin.readline().rstrip())
arr = [0] * N
for i in range(N):
    name, kor, eng, math = map(str,sys.stdin.readline().split())
    kor, eng, math = int(kor) , int(eng), int(math) # 점수들은 숫자로 변환
    arr[i] = [name , kor, eng, math] # 이중배열로 추가 

arr.sort(key=lambda z: (-z[1], z[2], -z[3], z[0])) # 문제에 나온 조건대로 정렬
for i in arr:
    print(i[0]) # 이름만 출력 