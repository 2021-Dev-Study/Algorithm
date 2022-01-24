# 파이썬에서 2진수로 바꾸는 법  : bin함수 사용 bin(N)하면 되는데 0b110101이 나옴
# do_it 89p 참고
# 10진법을 n진법으로 바꿀 때는 n으로 나눈 몫을 계속 나눠주고, 나머지는 역순으로 기입
# 재귀함수는 함수를 스택에 쌓는 것과 같아서 함수 안의 함수를 계속 스택에 넣고, 설정한 범위까지 넣었으면 pop해서 가장 마지막에 넣은 함수부터 실행시킨다.
N = int(input())
arr=[]
def binary_number(N):
    print("N : ", N)
    if N == 0:
        return
    else:
        binary_number(N//2)
        arr.append(N%2)
        print("arr : ", arr)

binary_number(N)

for i in arr:
    print(i, end='')

# N :  53
# N :  26
# N :  13
# N :  6 
# N :  3 
# N :  1
# N :  0
# arr :  [1]
# arr :  [1, 1]
# arr :  [1, 1, 0]
# arr :  [1, 1, 0, 1]
# arr :  [1, 1, 0, 1, 0]
# arr :  [1, 1, 0, 1, 0, 1]