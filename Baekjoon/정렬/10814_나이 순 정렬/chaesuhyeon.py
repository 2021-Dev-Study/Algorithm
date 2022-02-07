import sys
N = int(sys.stdin.readline().rstrip())
arr = []
idx = 0 # 순서 체크를 위한 변수

for _ in range(N):
    age , name = map(str, sys.stdin.readline().rstrip().split())
    age = int(age) # age를 int로 바꿔줌 
    idx += 1 
    arr.append([age, name, idx]) # 순서 체크를 위해서 idx도 append 

arr.sort(key=lambda z: (z[0], z[2])) # 나이를 기준으로 정렬하고, 나이가 같으면 idx를 기준으로 정렬하게 lamda사용

for i in range(N):
    print(arr[i][0], arr[i][1]) # 나이와 이름만 출력 