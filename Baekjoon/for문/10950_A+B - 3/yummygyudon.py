# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# 풀이 1 _ zip함수 활용
T = int(input())
A, B = [], [] # 입력받을 짝들의 각 위치의 값들을 넣을 리스트 생성

for i in range(T): # T. 즉, 입력받을 짝 갯수만큼 반복해서 각 리스트에 삽입
    a, b = map(int, input().split()) # 짝마다 A와 B 각각에 들어갈 숫자들로 나눠주기
    A.append(a)
    B.append(b)
for j, k in zip(A, B) : # zip함수로 다시 처음 입력받았던 순서대로 짝 맞춰주기 & j,k (구성값 갯수만큼) 더할 값으로 지정
    print(j+k)


# 풀이 2 _ 입력받는 시점마다 합값을 따로 저장 & 문자열 변환 후, join으로 출력
T = int(input())
result = []
for i in range(T): # T. 즉, 입력받을 짝 갯수만큼 반복해서 각 리스트에 삽입
    a, b = map(int, input().split())
    result.append(str(a+b))
print('\n'.join(result))