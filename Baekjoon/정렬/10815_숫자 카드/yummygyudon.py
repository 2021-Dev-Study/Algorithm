import sys
N = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
same = card & set(numbers.copy())
for i in range(M) :
    # 새로운 리스트를 위해 메모리 낭비 줄이기 위해 수정하는 방법
    if numbers[i] in same :
        numbers[i] = '1'
    else:
        numbers[i] = '0'
print(' '.join(numbers))

# 이진 탐색 ver => 런타입 에러 발생...ㅎ
def binary_search(arr, target, start,end) :
    while start <= end :
        mid = (start+end) //2

        if arr[mid] == target :
            return mid
        elif arr[mid] > target :
            end = mid-1
        else :
            start = mid+1
    return None # mid가 찾아지지 않을 때 -> 해당 값이 없을 때


N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for i in range(M) :
    if binary_search(card, numbers[i],0, N-1) is None :
        print(1, end='')
    else :
        print(0, end='')