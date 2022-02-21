# 어떤 자연수 N이 있을 때 , 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
# 어떤 자연수 M의 분해합이 N인 경우 M을 N의 생성자라고 함
# 자연수 N이 주어졌을 때 N의 가장 작은 생성자를 구하시오. 생성자가 없는 경우 0 출력

n = int(input())
for i in range(1, n+1): # 부르트 포스법 --> 앞에서부터 탐색함 완전탐색
    num = sum(map(int, str(i))) # i를 각 자리숫자를 문자열로 바꿔준 뒤 다시 int로 변환 후 합 계산
    n_sum = i + num # 숫자 + 각 자리수 합
    if n_sum == n:
        print(i)
        break
    if i == n: # i와 n이 같다는건 이미 실패함. 생성자 존재x (각 자리수를 더한 값도 포함이 되는데 이미 n과 같다는건 i에  각 자리수를 더했을때 값이 더 커짐 --> i는 생성자가 될 수 없음)
        print(0)