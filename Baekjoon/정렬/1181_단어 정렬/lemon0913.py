# 정렬 (단계별)
# 1181_단어 정렬

# sort는 문자열도 정렬해준다!!
import sys
if __name__ == "__main__":
    N = int(input())
    lst = [0]*N
    for i in range(N):
        lst[i] = sys.stdin.readline().replace("\n", "")

    # 중복 제거하기(set을 활용)
    set_lst = set(lst)
    lst = list(set_lst)

    lst.sort() # 먼저 사전 순으로 정렬하고
    lst.sort(key = len) # 길이 순으로 정렬하기

    for i in range(len(lst)):
        print(lst[i])