# level 7 - 문자열
# 2675번 문자열 반복



# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
# S에는 QR Code "alphanumeric" 문자만 들어있다.

# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 각 테스트 케이스에 대해 P를 출력한다.



#테스트 케이스마다 새 문자열로 바꾸는 함수
def change_str(L):
    #반복횟수(R)를 정수형으로 바꾸기
    L[0] = int(L[0])

    for i in range(2, len(L)):
        L[i] = L[i] * L[0]
    
    return L
    
    


if __name__ == "__main__":
    # 테스트케이스의 갯수와 각 테스트 케이스를 입력받기
    T = int(input())
    lst = [0] * T
    for i in range(T):
        #문자열은 튜플이라 수정이 불가능해 입력받은 문자열을 리스트로 바꾸는 과정이 필요함
        lst[i] = list(input())

    #테스트 케이스마다 새 문자열로 바꾸기
    for i in range(T):
        change_str(lst[i])

    #새 문자열 출력하기
    for i in range(T):
        for j in range(2, len(lst[i])):
            print(lst[i][j], end="")
        print()
    
   


            
        
    
    
        

           

    
    
