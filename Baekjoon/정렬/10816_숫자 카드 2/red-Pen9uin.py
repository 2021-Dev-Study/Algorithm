# 작성자: red-Pen9uin
# Classification: sort algorithm
# 10816_숫자 카드 2
# 수행 결과: 133784 KB / 1008 ms
"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.

정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""
"""
<상근이의 카드>
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.

둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

<구해야하는 카드>
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.

넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다.
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

<출력>
첫째 줄에 입력으로 주어진 M개의 수에 대해서,
각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
"""

import sys

def solution(cnt_sang, card_sang, cnt_many, how_many):
    card_sang.sort()

    # 이분탐색을 이용한 코드

    # get_cards = [0] * cnt_many

    # for i in range(cnt_many):
    #     left = 0 
    #     right = cnt_sang-1

    #     while left<=right:
    #         mid = (left+right)//2
    #         if card_sang[mid] == how_many[i]:
    #             # 같은 값을 갖는지 뒤로 체크
    #             tmp = mid
    #             while tmp < cnt_sang and card_sang[tmp] == how_many[i]:
    #                 get_cards[i] += 1
    #                 tmp += 1
    #             # 같은 값을 갖는지 앞으로로 체크
    #             tmp = mid-1
    #             while tmp >= 0 and card_sang[tmp] == how_many[i]:
    #                 get_cards[i] += 1
    #                 tmp -= 1
    #             break
    #         elif card_sang[mid]>how_many[i]:
    #             right = mid-1
    #         else :
    #             left = mid+1

    many_cards = set(card_sang)
    card_sang_cnt = {cards : 0 for cards in many_cards}

    for i in card_sang:
        try :
            card_sang_cnt[i] += 1
        except:
            pass

    get_cards = [0] * cnt_many
    j = 0

    for i in how_many:
        card = card_sang_cnt.get(i)
        if card:
            get_cards[j] = card
        else:
            pass
        j += 1
            

    return get_cards


if __name__ == "__main__":
    cnt_sang = int(sys.stdin.readline())
    sang = list(map(int, sys.stdin.readline().split()))

    cnt_many = int(sys.stdin.readline())
    how_many = list(map(int, sys.stdin.readline().split()))

    get_cards = solution(cnt_sang, sang, cnt_many, how_many)

    print(f" ".join(str(i) for i in get_cards))




"""
검색을 통해 찾은 다른 형태의 풀이
이진탐색 구현 후 count() 메서드를 이용해 구현
"""
# from sys import stdin
# _ = stdin.readline()
# N = sorted(map(int,stdin.readline().split()))
# _ = stdin.readline()
# M = map(int,stdin.readline().split())

# def binary(n, N, start, end):
#     if start > end:
#         return 0
#     m = (start+end)//2
#     if n == N[m]:
#         return N[start:end+1].count(n)
#     elif n < N[m]:
#         return binary(n, N, start, m-1)
#     else:
#         return binary(n, N, m+1, end)

# n_dic = {}
# for n in N:
#     start = 0
#     end = len(N) - 1
#     if n not in n_dic:
#         n_dic[n] = binary(n, N, start, end)

# print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))