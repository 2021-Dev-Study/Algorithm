# 어려운 문제라고...
# 모듈을 쓰라했는데
# 교재에서 병합정렬을 살펴보니 sorted()함수를 사용하네요

#메모리 : 83508KB / 시간 : 1404ms ㄷㄷ...;;
import sys
N = int(sys.stdin.readline())
a = []
for _ in range(N) :
    a.append(int(sys.stdin.readline()))

for num in sorted(a) :
    print(num)