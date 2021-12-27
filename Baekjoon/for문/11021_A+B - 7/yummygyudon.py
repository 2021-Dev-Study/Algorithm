# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# 10950 A+B - 3 문제의 풀이를 활용해서 풀었습니다! (해당 문제 풀이 참고)
# enumerate 함수 사용
T = int(input())
result = []
for i in range(T):
    a, b = map(int, input().split())
    result.append(a+b)
# 차이점은 print를 for문으로 바꾼 것 뿐..
for j, k in enumerate(result, start=1) :
    print(f"Case #{j}: {k}")