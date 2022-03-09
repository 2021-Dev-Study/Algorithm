# 문자열 검색
# 1057_토너먼트

# 왜 시간초과..??
# if __name__ == "__main__":
#     N, K, I = map(int, input().split())

#     cnt = 0
#     while True:
#         cnt += 1
#         # 임한수와 김지민이 붙었다면 몇 라운드에서 대결한 건지 출력
#         if K % 2 == 1 and I == K+1:
#             print(cnt)
#             break
#         # 임한수와 김지민이 붙지 않았다면 둘을 다음 라운드로 올리기
#         else:
#             K = (K + 1) // 2
#             I = (I + 1) // 2

# 토너먼트의 규칙..
if __name__ == "__main__":
    N, K, I = map(int, input().split())

    cnt = 0
    while True:
        K = (K + 1)//2
        I = (I + 1)//2

        cnt += 1
        if K == I:
            print(cnt)
            break