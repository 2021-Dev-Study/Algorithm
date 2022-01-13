# 작성자: red-Pen9uin
# Data structure: stack
# 23253: 자료구조는 정말 최고야
# 수행 결과: 57020 KB / 412 ms
"""
첫째 줄에 교과서의 수 $N$, 교과서 더미의 수 $M$이 주어진다.
둘째 줄부터 $2 x M$줄에 걸쳐 각 더미의 정보가 주어진다.

$i$번째 더미를 나타내는 첫 번째 줄에는 더미에 쌓인 교과서의 수 $k_{i}$ 가 주어지며,
두 번째 줄에는 $k_{i}$ 개의 정수가 공백으로 구분되어 주어진다.
각 정수는 교과서의 번호를 나타내며, 아래에 있는 교과서의 번호부터 주어진다.
교과서의 번호는 $1$부터 $N$까지의 정수가 한 번씩만 등장한다.
올바른 순서대로 교과서를 꺼낼 수 있다면 Yes를, 불가능하다면 No를 출력한다.

"""
import sys

# 계속 수행 시간 초과가 나는 코드.
# def arrange_books(books:list, total_num:int, total_stack:int) ->None:
#     count = 0

#     while count <= total_num:
#         count += 1
#         flag = False
#         for i in range(0, total_stack):
#             if len(books[i])==0:
#                 books.pop(i)

#             if len(books[i])>0 and (books[i][-1] == count):
#                 books[i].pop()
#                 flag = True
            
#         if not(flag):
#             break
    
#     if count == total_num:
#         print("Yes")
#     else:
#         print("No")
#     return


"""
스택에서 하나씩 꺼내는 방법으로 진행했었으나,
책을 어디에서 집어다가 꽂는지와 상관없이,
'순서대로' 책을 집을 수 있는가에 대한 문제.
"""
def arrange_books(books:list, total_num:int, total_stack:int) ->None:
    for i in range(0, total_stack):
        for j in range(0, len(books[i])-1):
            if books[i][j] < books[i][j+1]:
                print("No")
                return
    
    print("Yes")
    return


if __name__ == "__main__":
    total_num, total_stack = map(int, sys.stdin.readline().split())
    books = list()
    for _ in range(total_stack):
        num = int(sys.stdin.readline())
        books.append(list(map(int, sys.stdin.readline().split())))
    
    arrange_books(books, total_num, total_stack)

