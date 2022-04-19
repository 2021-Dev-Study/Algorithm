N = int(input())
arr = map(int, input().split())
arr.sort() # 숫자를 차례대로 더해주기 위해 정렬

result = 1 # 최솟값 처음에 1로 초기화 

for i in arr: # 숫자 하나씩 꺼내서 result랑 비교 
    if result < i:
        break
    else:
        result += i  # result - 1의 숫자는 만들 수 있음

print(result)

# 주어진 화폐 단위 [1,2,3,8]
# 1. result = 1, 화페 단위 1이 존재함으로 가능 -> result = 1 + 1 = 2 (2 이전의 모든 수는 표현이 가능하다는 의미)
# 2. result = 2, 화페 단위 2이 존재함으로 가능 -> result = 2 + 2 = 4(4 이전의 모든 수는 표현이 가능하다는 의미)
# 3. result = 4, 화페 단위 3이 존재함으로 가능 -> result = 4 + 3 = 7(7 이전의 모든 수는 표현이 가능하다는 의미)
# 4. result = 7, 다음 화페 단위는 8로 7을 만들 수 없음 -> 정답은 7