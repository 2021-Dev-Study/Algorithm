# 작성자: red-Pen9uin
# Classification: string search
# 17413_단어 뒤집기 2
# 수행 결과:  KB /  ms
"""
https://www.acmicpc.net/problem/17413

입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

출력
첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

"""
import sys

def solve(word):
    now = 0
    start = 0

    while now < len(word):
        if word[now] == "<": # do not reverse
            now += 1 
            while word[now] != ">":
                now += 1 
            now += 1
        elif word[now].isalnum(): # make reverse
            start = now
            while now < len(word) and word[now].isalnum():
                now+=1
            tmp = word[start:now]
            word[start:now] = reversed(tmp)
        else: # none
            now+=1

    print("".join(word))


reversed
if __name__ == "__main__":
    word = list(sys.stdin.readline().rstrip())

    solve(word)