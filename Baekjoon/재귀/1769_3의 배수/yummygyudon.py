# 예제 모두 맞지만 실패 _ 이유 모르겠음
# def is_multiple(n:str,cnt = 0) :
#     cnt += 1
#     # 밑에 조건문을 달았지만 실패
#     # if len(n) == 1 :
#     #     num = n
#     # else :
#     #     num = sum([int(s) for s in n])
#     num = sum([int(s) for s in n])
#     if len(str(num)) == 1 :
#         if int(num)%3 == 0 : #  in [3, 6, 9] 도 가능
#             return [cnt, "YES"]
#         else :
#             return [cnt, "NO"]
#     return is_multiple(str(num), cnt)
#
# input = input()
# for v in is_multiple(input) :
#     print(v)

# 이경우는 통과;;;
# 일단 질문은 등록해놓은 상태 => 스터디하기 전까진 답변이 오면 좋겠네요
def is_multiple(n:str,cnt = 0) :
    if len(n) > 1:
        cnt+=1
        num = sum([int(s) for s in n])
        is_multiple(str(num), cnt)
    else :
        if int(n) % 3 == 0:  # in [3, 6, 9] 도 가능
            print(cnt)
            print('YES')
        else :
            print(cnt)
            print('NO')
input = input()
is_multiple(input)