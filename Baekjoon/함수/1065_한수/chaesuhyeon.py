# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력

# 숫자 차이 구하는 것과 100이하의 수는 한수인 것 생각함. 근데 숫자를 쪼개는 코드를 몰라서 map함수 코드부분 참고함

def hansu(N):
    count = 0 # 한수의 개수 초기값
    
    for n in range(1, N + 1): # 1부터 ~ N까지 포함이 되어야 하므로 범위를 N + 1 까지 해줌
        array = list(map(int, str(n))) # 숫자를 문자로 변환한 뒤 하나씩 쪼갠 후 숫자로 다시 변환 
        if n < 100 :    # 100 이하 숫자들은 차이가 다 1로 모두 동일하므로 모두 한수임
            count += 1 
        elif (array[1]-array[0]) == (array[2]-array[1]): # 뒤 숫자랑 차이를 비교 , 3자리수까지 고려. 1000은 한수가 아님 
            count += 1
    return count

N = int(input()) # 숫자 입력 
print(hansu(N)) # 함수 호출 --> count return  // print안써줘서 틀림 