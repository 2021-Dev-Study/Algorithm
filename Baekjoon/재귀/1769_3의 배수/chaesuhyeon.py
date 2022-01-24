# 처음에 cnt를 매개변수로 안넣어줬더니 cnt집계를 잘 못함 
# cnt도 매개변수로 넣어줌
def three(N , cnt): 
    if len(N) > 1: # 숫자의 길이가 2자리수일때까지 반복문 실행 
        sum = 0
        cnt += 1
        for i in N: # 숫자지만 문자열이기 때문에 i로 하나씩 받아와서 int로 바꿔준 후 sum에 누적합 해줌 
            sum += int(i)
        three(str(sum), cnt) # sum을 다시 문자열로 바꿔줘서 N으로 넘김 --> 다시 three함수가 실행돼서 len(N)길이 판단(한자리 수 될 때 까지)
    else: # 숫자가 한자리수이면 그 수를 3으로 나눴을 때 나머지가 0이면 3의 배수 
        if int(N) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

N = input()
cnt = 0
three(N , cnt)

