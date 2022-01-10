import sys


book_cnt, dummy_cnt = map(int, sys.stdin.readline().rstrip().split(" "))
stack = []
#books = [x for x in range(1, book_cnt + 1)]
books = [x for x in range(book_cnt, 0, -1)]
# answer = ""
status = ""
for i in range(dummy_cnt):
    n = int(sys.stdin.readline().rstrip())
    temp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    stack.append(temp)

## 시간 초과
# for book_num in books:
#     for dummy in stack:
#         if dummy:
#             if dummy[-1] == book_num:
#                 dummy.pop()
#                 status = True
#                 break
#             else:
#                 status = False
#     if status == False:
#         break


# print("Yes") if status == True else print("No")
    
# while books:
#     count = 0
#     book_num = books.pop()
#     for dummy in stack:
#         if dummy:
#             if dummy[-1] == book_num:
#                 dummy.pop()
#                 break
#             else:
#                 count += 1
#     if count == dummy_cnt:
#         answer = "No"
#         break
#     else:
#         for dummy in stack:
#             if dummy:
#                 answer = "No"
#                 break
#         answer = "Yes"


# print(answer)

## 찾아봄.,.. 스택문젠데 스택 사용하지 말라는 건,,

for dummy in stack:
    for i in range(len(dummy)-1):
        if dummy[i] < dummy[i+1]:
            status = False
            break
    if status == False:
        break
print("No") if status == False else print("Yes")