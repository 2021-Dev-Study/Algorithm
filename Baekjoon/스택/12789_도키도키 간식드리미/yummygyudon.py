

import sys

# 임시 줄 스택에는 큰순서대로 밑에 들어가게되면 성공적으로 들어가서 쌓였다가 나올 수 있다.
# 그런데 또 틀림... 백준을 신뢰할 수가 없다..
n = int(sys.stdin.readline())
line = [int(num) for num in sys.stdin.readline().rstrip().split()]
stk = []
result = "Nice"
t = 0
for i in range(len(line)) :
    if line[i] == t+1 : # 이전 순번 다음 번호(t+1)일 경우
        t += 1 # 넘어갔다는 가정과 함께 다음 번호를 위해 +1
    elif line[i] > t+1 : # 이번에 와야할 번호보다 큰 번호일 경우
        if stk : # stk안에 이미 다른 값이 있는데
            if stk[-1] > line[i] : # 순서와는 안맞는 이번 번호보다 클경우 들어가도 됨.
                stk.append(line[i]) # 삽입
            else : # 이번에 들어갈 숫자가 더 크면 밑에 숫자가 나올 수 없기 때문에 순서대로 받는 것 불가능
                result = "Sad" # Sad를 부여하고
                break # 반복문 끝내기
        else : # stk 안에 아무 값도 없을 때
            stk.append(line[i])
# if stk :
#     for _ in range(len(stk)) :
#
print(result)