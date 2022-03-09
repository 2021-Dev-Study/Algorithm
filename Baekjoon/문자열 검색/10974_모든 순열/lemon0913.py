# 문자열 검색
# 10974_모든 순열

from itertools import permutations
if __name__ == "__main__":
    # N을 입력받아 1~N까지의 수를 배열에 저장
    N = int(input())
    nums = list(range(1, N+1))
    
    # 1부터 N까지의 수로 이루어진 순열을 구하기
    per_list = list(permutations(nums, N))

    # per_list의 각 원소는 set의 형태라서 list의 형태로 바꾸기
    for i in range(len(per_list)):
        per_list[i] = list(per_list[i])
        
        # per_list의 각 원소들을 출력
        for j in range(N):
            print(per_list[i][j], end=' ')
        print()
    