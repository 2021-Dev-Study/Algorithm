# level 5 - 1차원 배열
# 2562번 최댓값

# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 
# 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.




#배열 안에 key 값이 몇 개 들어 있는지 구하는 함수 정의
def seq_search(ary, key) :
    num = 0
    for i in range(len(ary)):
        if ary[i] == key:
            num = num + 1
    return num

if __name__ == "__main__" :
    #A, B, C 입력받기
    A = int(input())
    B = int(input())
    C = int(input())
    N = A*B*C
   
    #배열 선언하기
    ary = [10] * 10
    i = 0

    #배열의 원소로 A*B*C의 각 자리수 넣기 
    while N >= 1 :
        ary[i] = N%10
        N = int(N/10)
        i = i+1

    print(seq_search(ary, 0))
    print(seq_search(ary, 1))
    print(seq_search(ary, 2))
    print(seq_search(ary, 3))
    print(seq_search(ary, 4))
    print(seq_search(ary, 5))
    print(seq_search(ary, 6))
    print(seq_search(ary, 7))
    print(seq_search(ary, 8))
    print(seq_search(ary, 9))


    


# 빈 배열을 선언하고 싶어서 ary = [] 하니 에러남
# 그래서 10개의 10으로 채워진 배열을 선언했음.
