# 정렬 (단계별)
# 10989_수 정렬하기 3

# 수의 범위가 작다면 카운팅 정렬을 사용하면 더 빨리 정렬할 수 있다.
# 카운팅 정렬의 이해를 돕기 위해 step 별로 보기 -> (https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html)


# import sys

# if __name__ == "__main__":
#     # 수의 개수 N과 N개의 수 입력받기
#     N = int(input())
#     lst = []
#     for i in range(N):
#         lst.append(int(input()))
    
#     # lst의 각 요소의 출현횟수를 저장하는 count 리스트와
#     # 정렬된 결과를 저장하는 result 리스트를 생성
#     count = [0] * (max(lst)+1)
#     result = [0] * len(lst)

#     # counting 배열에 주어진 lst의 각 요소 출현 횟수를 담는다
#     for i in lst:
#         count[i] += 1

#     # counting 배열에서 누적 counting을 구한다
#     for i in range(len(count)-1):
#         count[i+1] += count[i]

#     for i in range(len(lst)-1, -1, -1): # lst의 요소 값을 뒤에서부터 가져온다
#         result[count[lst[i]]-1] = lst[i]  # counting의 값으로 index를 찾고 result 배열에 넣기
#         count[lst[i]] -= 1 # 누적 counting 값에서 -1 하기

#     for i in result:
#         print(i)


# 카운딩 정렬 쓰래서 썼더니 메모리 초과..
# 카운딩 정렬 비슷?하게 풀어봄 -> 입력받은 값의 출현 횟수를 세서 푸는 방식
# for문 안에서 append를 사용하면 메모리 재할당이 이루어져 메모리를 효율적으로 사용하지 못함
import sys

if __name__ == "__main__":
    N = int(input())
    count = [0] * 10001
    # count 리스트에 입력값의 출현 횟수를 저장
    for _ in range(N):
        count[int(sys.stdin.readline())] += 1

    # count 리스트의 값이 0이 아니다 -> 리스트의 요소 값 만큼 인덱스 값을 출력
    for i in range(10001):
        if count[i] > 0:
            for j in range(count[i]):
                print(i)