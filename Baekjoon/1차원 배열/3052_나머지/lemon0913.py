# level 5 - 1차원 배열
# 3052번 나머지



# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 
# 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.





#배열 안에서 중복 되는 원소가 있으면 그 중 하나를 제외하고 나머지는 43으로 바꾸는 함수
def compare_element(ary):
    
    for i in range(10):
        for j in range(i+1, 10):
            if ary[j] == ary[i]:
                ary[j] = 43
    
    count_not_43(ary)


#배열의 원소 중 43이 아닌 원소의 개수 구하기
def count_not_43(changed_ary):
    num = 0
    for i in range(10):
        if changed_ary[i] == 43:
            num = num + 1
        
    print(10-num)
     

if __name__ == "__main__":
    
    #서로 다른 원소의 갯수를 세기 위해 정의한 변수
    N = 0

    #10칸짜리 배열 선언 한 뒤, 입력받은 10개의 숫자로 배열 채우기
    a = [0] * 10
    for i in range(10):
        a[i] = int(input())%42
    
    compare_element(a)
    