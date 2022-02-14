# 11652	: 카드

'''
가장 많이 가지고 있는 정수를 구하는 프로그램을 작성
'''
# from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
# n_list = [int(input()) for _ in range(n)] # [1, 2, 1, 2, 1]

# n_count = Counter(n_list).most_common()   # [(1, 3), (2, 2)]
# print(n_count[0][0])

n_dic = {}

for i in range(n):
    num = int(input())
    if num in n_dic:
        n_dic[num] += 1
    else:
        n_dic[num] = 1

n_dic = sorted(n_dic.items(), key=lambda x: (-x[1], x[0]))  # -x[1] : 카드 개수 기준으로 내림차순 정렬
                                                            #  x[0] : 카드 값을 기준으로 오름차순 정렬
print(n_dic[0][0])