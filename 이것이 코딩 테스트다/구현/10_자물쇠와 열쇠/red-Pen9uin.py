# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# Classification: Implementation algorithm
# 10_자물쇠와 열쇠

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

"""
[[0, 0, 0],
 [1, 0, 0],
 [0, 1, 1]]

[[1, 1, 1],
 [1, 1, 0],
 [1, 0, 1]]
"""


def rotate_NxN(key):
    row = len(key)
    col = len(key[0])

    new_key = [[0]*col]*row

    for i in range(row):
        for j in range(col):
            # print(i,j)
            new_key[j][row - i - 1] = key[i][j]

    return new_key

#키가 자물쇠에 맞는지 확인
def check(lock_padding):
    lock_length = len(lock_padding) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if lock_padding[i][j] != 1:
                return False
    return True

#키를 자물쇠에 넣었을때
def keyIn(lock_padding, key):
    n = len(lock_padding) // 3
    for x in range(n*2):
        for y in range(n*2):
            for i in range(len(key)):
                for j in range(len(key)):
                    lock_padding[x + i][y + j] += key[i][j]
            if check(lock_padding) == True:
                return True
            for i in range(len(key)):
                for j in range(len(key)):
                    lock_padding[x + i][y + j] -= key[i][j]
    return False

def solution(key, lock):
    n = len(lock)
    rotate_count = 0
    lock_padding = [[0] * (n*3) for _ in range(n*3)] #새로운 자물쇠 만들기
    for i in range(n):
        for j in range(n):
            lock_padding[i + n][j + n] = lock[i][j]
    while True:
        answer = keyIn(lock_padding, key)
        if answer or rotate_count == 3:
            break
        else:
            key = rotate_NxN(key)
            rotate_count += 1
    return answer

if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    solution(key, lock)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""