N = int(input())
# ls = [1, 2, 3]

result = []

# 재귀함수 자체에 같은 변수 써서 별도 변수 선언이나 매개변수설정 안했습니다
def setting() :
    if len(result) == N : # 종료조건 ( 삽입된 숫자들 갯수가 길이와 같을 경우)
        # print(result)
        print(' '.join(map(str,result))) # 리스트 내의 숫자들 붙여서 출력
        return
    for i in range(1, N+1) :
        if i not in result :
            result.append(i)
            setting()
            result.pop() # 나오면서 result내부 LIFO 방식으로 빼주면서 초기화
setting() 

# tmp = ""
#
# for i in range(len(ls)) :
#     cnt = 0
#     used = []
#     tmp += str(ls[i])
#     used.append(ls[i])
#     cnt += 1
#     for k in range(len(ls)-cnt) :
#         if k in used :
#             continue
#         tmp += str(ls[k])
#         used.append(ls[k])
#         for j in range(len(ls)):
#             if j in used:
#                 continue
#             tmp += str(ls[j])
#             print(tmp)
#             tmp =""
#             used.append(ls[j])