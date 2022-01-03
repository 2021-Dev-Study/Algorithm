# level 5 - 1차월 배열
# 10818번 최소, 최대

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다. 
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

#배열의 최댓값을 구하는 함수 정의
def find_max(a) :
    max = a[0]
    for i in range (1, len(a)):
        if a[i] > max:
            max = a[i]
    return max

#배열의 최솟값을 구하는 함수 정의
def find_min(a) :
    min = a[0]
    for i in range (1, len(a)):
        if a[i] < min:
            min = a[i]
    return min

#######메인 함수 부분#######  
N = int(input())
ary = list(map(int, input().split())) #배열의 원소 입력받기

#함수를 사용해 배열의 최대, 최소값 구하기
max_value = find_max(ary)
min_value = find_min(ary)

print(f'{min_value} {max_value}')
