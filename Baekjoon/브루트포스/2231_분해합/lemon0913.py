# 브루트포스
# 2231_분해합


if __name__ == "__main__":
    N = int(input())

    # 자연수 N보다 작은 수에 대해서 순차적으로 분해합을 구하기
    for i in range(N):
        x = i
        sum = i
        while i>0:
            sum += i % 10
            i = i // 10
        
        # 만약 분해합이 N과 같다면 그 자연수를 출력
        if sum == N:
            print(x)
            break
        # 만약 생성자가 없다면 0을 출력
        elif x == N-1:
            print(0)
  
    
