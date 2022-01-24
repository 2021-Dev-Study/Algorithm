# def make_biggest(limit_len, limit_num ,value =0, temp=0 ) :
#     if limit_len == 1 :
#         for num in numbers:
#             temp = num
#             if temp <= int(limit_num) :
#                 value+=temp
#                 break
#         print(value)
#     else :
#         if limit_num[0] == '0' :
#             limit_num = str(limit_num)[1:]
#             make_biggest(limit_len - 1, limit_num, value)
#         else :
#             pos = 10**(limit_len-1)
#             for num in numbers :
#                 temp = num*pos
#                 if temp <= (int(limit_num)//pos)*pos :
#                     value += temp
#                     break
#             make_biggest(limit_len-1,str(limit_num)[1:],value)

def make_biggest(pos=0, n=0) :
    # 각 재귀에서 return 되었을 때 비교해줄 수있는 값
    # 가장 아래 단계에서부터 처음값 0과 비교되면서 올라옴
    # 올라가면 앞단계에서의 max값이 계속 올라오게됨
    # 종료 조건을 위해 사용하는 변수
    global each_v
    # 종료조건
    if pos == Length : # 가장 오른쪽 자리까지 내려왔을 때 (Num의 길이와 같을 때)
        # (Length - 1) - pos)의 값이 0이 될때 : 자릿수만큼 pos가 늘어서 도착한 상태

        if not '0' in str(n) : # 1의자리 수가 0일 때를 대비
            each_v = max(each_v, n) # 0과 여태 누적합했던 값
        # 0이라면 그냥 each_v 0으로 시작
        return


    for i in range(k) :
        # TIP - 0제곱은 1
        tmp = numbers[i] * ( (10** ((Length-1) - pos)) ) +n # 이전 함수의 누적합을 더해주기
        # 100의 자리는 3자리(Length)지만 10의 "2"제곱 pos를 빼는 것은
        # 오른쪽 자리로 내려가는 재귀호출 -> 100의자리 -> 10의자리 -> 1의자리

        # Num안의 0과 마주치면 else 문으로 돌아서
        if tmp <= Num : # 작은 숫자는 여러개가 들어갈 수 있음
            make_biggest(pos + 1, tmp)
        else : # Num안에 0이 들어가서 비교하면 항상 작은 경우
            # 0이 나온다면 numbers에 있는 수들보다 작을 수 밖에 없으니 건너 뛰고 바로 재귀호출
            make_biggest(pos + 1, n)

# ex 300 1
#    {7 5 1}
# 1차 : 100으로
# (pos = 1)
# 2차 : 170(1) | 150(2) | 110(3)
# (pos = 2)
# 3차 : 177(1-1) -> 175(1-2) -> 171(1-3) | 157(2-1) -> 155(2-2) -> 151(2-3) | 117(3-1) -> 115(3-2) -> 111(3-3)
#  > each_v와 비교
# 177과 0 비교 -> each_v == 177
# (each_v global 변수 로 지정되서 (1-2)재귀하러 넘어감 )
# 위 과정 반복 [ 1차 -> 2차 -> 3차 -> 2차 다음 for문 -> 3차 -> 2차 다음 for문 ...

## 메모리 : 30860KB / 시간 : 76ms

import sys
Num ,k  = map(int,sys.stdin.readline().rstrip().split())
Length = len(str(Num))
numbers =  list(map(int,sys.stdin.readline().rstrip().split()))
numbers.sort(reverse=True)
each_v = 0

make_biggest()
print(each_v)



