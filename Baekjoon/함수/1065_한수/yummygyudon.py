# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 일단 1~99까지는 모두 한수임._등차를 측정할 수 없거나 하나일 경우밖에 없음
# 111까지의 모든 수들의 한수 갯수는 99이고 두 자릿수들까지는 모두 자기 자신이 한수 갯수임.
# 1000보다 작기 때문에 999까지인데 (첫자리&둘째자리 차) 와 (둘째자리 & 셋째자리 차)만 비교하면됨.

def hannum(n) :
    if n < 100 :
        return n
    else :
        i = 100 # 세자릿수 시작인 100부터 입력값까지만 각 자릿수 차이 비교하면됨.
        b = 99 # 세자리수 이전 기본 한수값
        while i <= n :
            num = [int(s) for s in str(i)]
            x,y = num[0]-num[1], num[1]-num[2]
            if x == y :
                b+=1 #각자리가 등차수열일 경우
            i+=1 # 입력값이 될때까지 루프돌때마다 더해줘야함.
        return b

print(hannum(int(input())))