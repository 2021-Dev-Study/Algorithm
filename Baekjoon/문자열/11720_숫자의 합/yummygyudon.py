# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
#
# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

# 첫째줄 입력값을 사용해야할 것 같아서 for문 사용했습니다.
import sys
n = int(sys.stdin.readline().rstrip())
s = str(sys.stdin.readline().rstrip())
v = 0
for i in range(n):
    v += int(s[i])
print(v)

# 사용X
#for문 말고
print(sum([int(num) for num in s ]))