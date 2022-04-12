from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_set = set()
    
    def is_prime(nums_set):
        check = []
        flag = False
        for num in nums_set:
            # 0과 1은 소수가 아님
            if num == 0 or num == 1:
                continue
            # 얼추 반저리 이후부터는 나눌 수가 없음    
            for i in range(2, num//2 + 1):
                # 소수가 아닐 경우: 딱 나누어 떨어질 때 -> 다음 숫자로 넘어가기(소수 확인 루프 탈출)
                if num % i == 0:
                    flag = True
                    break
            # 소수확인 루프 종료시 소수가 아닐경우 flag True -> 다시 False로 바꾸고 다음 넘버로 넘어감
            if flag:
                flag = False
                continue
            else: # 소수가 맞는 경우 flag는 변화 없기 때문에 True를 check에 넣어줌
                check.append(True)
        return len(check)
    
    numbers_list = list(numbers)
    numbers_comb = []
    for i in range(1, len(numbers) + 1):
        numbers_comb.append(list(permutations(numbers_list, i)))
    
    for comb_list in numbers_comb:
        comb_list = list(set(comb_list))
        
        for comb in comb_list:
            numbers_set.add(int("".join(comb)))

    return is_prime(numbers_set)