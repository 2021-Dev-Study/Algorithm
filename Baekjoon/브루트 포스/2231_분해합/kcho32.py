## 0부터 해당 숫자까지 모든 수를 비교 --> 비교적 오래 걸린다
# n = int(input())
# answer = 0

# for i in range(n):
#     tmp = i
#     tmp_sum = i
#     while True:
#         if tmp == 0:
#             break
#         else:
#             tmp_sum += tmp % 10
#             tmp //= 10
#     if tmp_sum == n:
#         answer = i
#         break

# print(answer)

## 범위 제한 두기
n_str = input()
n = int(n_str)
answer = 0
start = 10 ** (len(n_str) - 2)

# 1~9일 때, 홀수일경우는 불가, 짝수일 경우는 1/2값이 정답
# 10 이상일 경우 n//10 자리 수 이상으로 계산
# 거의 효과 없음...
if n <= 10:
    if n % 2:
        answer = 0
    else:
        answer = n // 2

else:
    for i in range(start, n):
        tmp = i
        tmp_sum = i
        while True:
            if tmp == 0:
                break
            else:
                tmp_sum += tmp % 10
                tmp //= 10
        if tmp_sum == n:
            answer = i
            break

print(answer)