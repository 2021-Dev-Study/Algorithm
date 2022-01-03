# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

# 10950 A+B - 7 문제의 풀이를 활용해서 풀었습니다! (해당 문제 풀이 참고)
T = int(input())
result = []
for i in range(T):
    a, b = map(int, input().split())
    # 차이점은 리스트 객체로 추가하여 저장한 것
    result.append([a, b, a+b])
for j, k in enumerate(result, start=1) :
    #각 index에 위치한 값들 가져오기
    print(f"Case #{j}: {k[0]} + {k[1]} = {k[2]}")