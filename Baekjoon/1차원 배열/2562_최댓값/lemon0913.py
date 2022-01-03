# level 5 - 1차월 배열
# 2562번 최댓값

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.



#최댓값을 구하는 함수 정의
def find_max(a) : 
    max = a[0]
    
    for i in range(1, len(a)):
        if max < a[i]:
            max = a[i]
    
    return max


#key값의 인덱스를 구하는 함수 정의 - 이진탐색(for문을 활용)
def find_index(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


if __name__ == "__main__":
    
    ary = ['0'] * 9

    #크기가 9인 배열의 원소 입력받기
    for i in range(9):
        ary[i] = int(input())
    
    max_value = find_max(ary)
    index = find_index(ary, max_value)

    print(max_value)
    print(index+1)

    




