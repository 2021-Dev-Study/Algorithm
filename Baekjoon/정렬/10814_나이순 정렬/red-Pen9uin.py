# 작성자: red-Pen9uin
# level 12: sort algorithm
# 10814_나이순 정렬
# 수행 결과: 50856 KB / 1128 ms
"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로,
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

"""
import sys


def solution(word):
    # solve = quick_sort(num, 0, len(num)-1)
    solve = merge_sort(word)
    return solve


def merge_sort(word):
    
    def _merge_sort(word, left: int, right: int) -> None:

        if left < right: # 조건을 만족할 경우에만 재귀 발생
            center = (left+right)//2

            _merge_sort(word, left, center)
            _merge_sort(word, center+1, right)

            p_index = p_buff = 0
            p_word = index = left

            while p_word <= center: # buff에 복사
                buff[p_index] = word[p_word]
                p_word += 1
                p_index += 1
            
            while p_word <= right and p_buff < p_index: # 병합
                if int(buff[p_buff][0]) <= int(word[p_word][0]): # 나이 오름차순
                    word[index] = buff[p_buff]
                    p_buff += 1
                else:
                    word[index] = word[p_word]
                    p_word += 1
                index += 1

            while p_buff < p_index: # 나머지 병합
                word[index] = buff[p_buff]
                p_buff += 1
                index += 1
        # end of _merge_sort

    buff = [None] * len(word)
    _merge_sort(word, 0, len(word)-1)
    del buff

    return word


if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    word = list()
    for _ in range(cnt):
        word.append(tuple(sys.stdin.readline().split()))

    # print(word)
    word = solution(word)
    for w in word:
        print(f"{w[0]} {w[1]}")