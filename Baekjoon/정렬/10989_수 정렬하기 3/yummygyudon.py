# ## 메모리 초과가 떴네요...
# def Counting_Sort(ary, max) :
#     n = len(ary)
#     freq = [0] * (max+1)
#     tmp = [0] * n
#
#     # 누적도수분포가 정렬 index로 활용되는 방법
#     for i in range(n) :
#         # ary[i]로는 각 자리에 해당하는 값들
#         # 그 값 -> freq의 index로 활용 _ 빈도수
#         freq[ary[i]] += 1
#     for i in range(1, max+1) :
#         # 두번째 요소부터 전값을 더하면 됨.
#         freq[i] += freq[i-1]
#     for i in range(n-1, -1, -1) :
#         # 역순으로 자리배치 해야 값들의 순서가 순서대로 배치됨.
#         freq[ary[i]] -= 1 # ary 맨 오른쪽에 있는 값의 빈도수는 1 빼주고
#         tmp[freq[ary[i]]] = ary[i]# ary 맨 오른쪽에 있는 값의 index에 그 값이 들어감.
#     for i in range(n) :
#         ary[i] = tmp[i]



# 도저히 풀 수 있는 방법을 모르겠고... 8MB 안에 어떻게하나 싶어서..
# 알아보았습니다

# 동일한 Counting Sort이긴 하나
# 애초에 배열을
# 수의 한계인 10000보다 작거나 같다라는 조건을 적용시켜
# 크게 잡고 해당값의 index로 사용하고 누적시키고

# 중요한 것은 재배치하지 않고 앞에서부터 10001번째까지 쭉 훓으면서
# 1이상 출현한 값들을 for문으로 그 빈도수 만큼 해당 값을 출력시켜주는 것이다.

# 시간은 비록 8596ms이지만
# 메모리는 30860KB를 사용했네요
import sys
N = int(sys.stdin.readline())
ary = [0] * 10001 #수의 한계만큼 배열만들기
# 누적빈도수
for i in range(N) :
    ary[int(sys.stdin.readline())] += 1
#완료 후
# 앞에서부터 빈도수 확인
# 1 이상이면 빈도수만큼 그 값 반복 출력
for i in range(10001) : # len()등의 함수를 쓰기 보단 정수를 쓰는것이 효율적
    if ary[i] >= 1 :
    # sys.stdout.write를 하면 메모리 초과를 면할 수 있다고 합니당
        for k in range(ary[i]) :
            sys.stdout.write(str(i)+'\n')