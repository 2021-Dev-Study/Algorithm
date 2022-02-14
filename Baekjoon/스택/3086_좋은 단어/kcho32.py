import sys


n = int(input())
answer = 0
# BABBAB 반례 같은거 사이에 다른게 홀수개여도 작동하는 예시
# for i in range(n):
#     temp = []
#     count = 0
#     str = list(sys.stdin.readline().rstrip()[::-1])
#     first = str.pop()
#     temp.append(first)
#     while len(str):
#         x = str.pop()
#         if x != first:
#             count += 1
#             temp.append(x)
#         elif x == first:
#             temp.append(x)
#             if count % 2 == 0:
#                 if len(str):
#                     first = str.pop()
#                     temp.append(first)
#                 else:
#                     answer += 1
#                     break
#             else:
#                 break
        
# print(answer)

for i in range(n):
    temp = []
    ## 받은 문자열을 거꾸로 입력
    str = list(sys.stdin.readline().rstrip()[::-1])
    temp.append(str.pop())
    
    while True:
        if str:
            x = str.pop()
            if len(temp):
                if x == temp[-1]:
                    temp.pop()
                else:
                    temp.append(x)
            else:
                temp.append(x)
        else:
            if len(temp) == 0:
                answer += 1    
            break

print(answer)
