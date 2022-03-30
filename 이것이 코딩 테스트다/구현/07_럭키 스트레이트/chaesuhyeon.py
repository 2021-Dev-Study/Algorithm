# 풀이 1
n = input() # 길이 측정을 위해 문자열로 입력받음
mid = len(n)//2 # 반으로 가른 위치

left = n[:mid] # 왼쪽
right = n[mid:] # 오른쪽

sumleft = 0 # 합계를 위한 변수
sumright = 0

for i in range(mid): # left와 right에 저장된 값들의 합을 구함
    sumleft += int(left[i])
    sumright += int(right[i])

if sumleft == sumright: # 두개의 합이 같다면 럭키
    print("LUCKY")
else:
    print("READY")


# 풀이 2
n = list(input()) # 길이 측정을 위해 문자열로 입력받음
mid = len(n)//2 # 반으로 가른 위치
sumleft = 0
sumright = 0

while True:
    sumright += int(n.pop()) # 뒤부터 숫자 뽑아서 오른쪽 합계에 더해줌 
    if len(n) == mid: # n의 길이가 mid가 되면 반복문 종료 (pop 그만..)
        break

for i in range(mid): # 남은 n (왼쪽부분)의 합계를 구해줌
    sumleft += int(n[i])

if sumleft == sumright: # 두개의 합이 같다면 럭키
    print("LUCKY")
else:
    print("READY")

####################################### 책풀이
n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")

