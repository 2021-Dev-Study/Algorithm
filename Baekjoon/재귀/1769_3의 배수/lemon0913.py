# 재귀 (단계별 & 실버5)
# 1769_3의 배수

# 시간초과
# def multiple3(x, c):
#     Y = 0 # 각 자리수 합 구하기
    
#     while x > 0 :
#         Y += (x%10)
#         x = x // 10
    
#     # 변환 과정 1번 수행했으니까 c 1증가
#     c += 1

#     if Y >= 10: # 변환 과정을 거친 후 Y가 한 자리 수가 아니라면
#         multiple3(Y, c)
#     else: # 변환 과정을 거친 후 Y가 한 자리 수라면
#         print(c)
#         if Y % 3 == 0 : # Y가 3의 배수라면
#             print('YES')
#         else: # Y가 3의 배수가 아니라면
#             print('NO')



# if __name__ == "__main__":
#     X = int(input())
#     count = 0 # 변환 과정을 몇 번 수행했는지 구하는 변수

#     multiple3(X, count)




# 그냥 문자열로 입력받으면 각 자리수를 구하는 과정, 변환 결과가 한 자리수 인지 판단하는 과정이 없어짐 -> 시간 단축 가능

def multiple3(x, c):
    
    if len(x) > 1: # 한 자리수가 될 때 까지 변환하기
        c += 1 # 변환 횟수
        Y = 0 # 변환 결과
        for i in x:
            Y += int(i) # 각 자리수 더하기
        multiple3(str(Y), c) 
    
    else: # 한 자리수가 되면
        if int(x) % 3 == 0 : #x가 3의 배수라면
            print(c)
            print('YES')
        else: # x가 3의 배수가 아니라면
            print(c)
            print('NO')


if __name__ == "__main__":
    X = input()
    count = 0 # 변환 횟수
    multiple3(X, count)





