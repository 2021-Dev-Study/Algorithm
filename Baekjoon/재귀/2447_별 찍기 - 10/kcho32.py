"""
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
"""

# def stars(n):
#     if n > 1:
#         answer = ""
#         for i in range(1, 4):
#             for j in range(1, 4):
#                 if not i%2 and not j%2:
#                     answer += " " * (n//3)
#                 else:
#                     answer += stars(n//3)
#             answer += "\n"
#         return answer
#     elif n == 1:
#         return "*"

# print(stars(9))

## answer를 str로 하려했을 때 문제 발생

def stars(n, star_list):
    answer = []
    if n <= 3:
        return star_list
    else:
        ## 맨 처음엔 "***", "* *", "***"
        ## answer리스트에는 ["***" * 3, "* *" * 3, "***" * 3]가 들어가게 된다
        for i in star_list:
            answer.append(3 * i)
        
        ## 중앙의 빈 부분
        for j in star_list:
            answer.append(j + " " * len(j) + j)
        
        ## 하단 (처음과 같음)
        for i in star_list:
            answer.append(3 * i)

        return stars(n//3, answer)
        

print("\n".join(stars(int(input()), ["***", "* *", "***"])))
