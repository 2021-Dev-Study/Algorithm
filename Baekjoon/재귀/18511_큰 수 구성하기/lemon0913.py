# 재귀 (단계별 & 실버5)
# 18511_큰 수 구성하기

# 순열이지만 중복을 허용 -> product
# 왜 재귀..? product를 재귀로 구현할 수 있음.. 
from itertools import product

if __name__ == "__main__":
    N, K = list(map(int, list(input().split())))
    num = list(map(str, list(input().split())))
    length = len(str(N))

    while True:
        # num 배열에서 N의 자릿수만큼 숫자를 뽑아 곱순열 리스트 만들기
        prod = list(product(num, repeat = length))
        result = []
        for i in prod:
            tmp = int(''.join(i)) # 곱순열의 원소를 합쳐서 자연수로 바꾸기
            if tmp <= N: # 만들어진 자연수가 N보다 작거나 같을때만 result 배열에 추가
                result.append(tmp)
        
        if len(result) >= 1: # result 배열이 만들어졌다면 거기서 최대값 출력
            print(max(result))
            break
        # result배열이 만들어지지 않았다 
        # -> N의 자리수가 K보다 커서 prod 배열이 만들어지지 않은 것 
        # 예를들어 N=1938, K배열은 {8,9,4}면 출력해야하는 수는 999이지만 N은 4자리수고 K는 3이여서 product(num, repeat = length)에서 곱순열을 만들지 못한다
        # -> product(num, repeat = length) 에서 곱순열이 만들어질 때 까지 repeat을 줄이자
        else: 
            length -= 1
        


    
    

    
    
