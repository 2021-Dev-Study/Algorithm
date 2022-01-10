import sys


nums = int(sys.stdin.readline().rstrip())
# first = [x for x in range(nums, 0, -1)]
# second = []
# last = False

# for i in range(nums):
#     goal = int(sys.stdin.readline().rstrip())
#     try:
#         if goal > first[-1]:
#             while True:
#                 if first[-1] == goal:
#                     first.pop()
#                     print('+')
#                     print(first, second, end="\n")
#                     break
#                 x = first.pop()
#                 second.append(x)
#                 print('+')
#                 print(first, second, end="\n")
        
#         elif goal < first[-1]:
#             while True:
#                 if second[-1] == goal:
#                     second.pop()
#                     print('-')
#                     print('-')
#                     print(first, second, end="\n")
#                     break
#                 x = second.pop()
#                 first.append(x)
#                 print('-')
#                 print(first, second, end="\n")

#     except:
#         print("No")            





# goals = [int(sys.stdin.readline().rstrip()) for i in range(nums)]
# inputs = [x for x in range(nums, 0, -1)]

# stack = []
# answer = ""
# answer_list = []
# for goal in goals:
#     if answer != "NO":
#         while True:
#             if len(stack):
#                 if stack[-1] == goal:
#                     stack.pop()
#                     answer_list.append('-')
#                     break
#                 elif stack[-1] != goal and goal in stack:
#                     answer = "NO"
#                     break
#                 # elif stack[-1] > goal:
#                 #     inputs.append(stack.pop())
#                 #     answer += '+'
#             if inputs[-1] <= goal:
#                 stack.append(inputs.pop())
#                 answer_list.append('+')
# if answer == "NO":
#     print(answer)
# else:
#     print("\n".join(answer_list))




## 뭐뭐 in list는 시간이 오래 걸리므로 사용하지 말자...
goals = [int(sys.stdin.readline().rstrip()) for i in range(nums)]
inputs = [x for x in range(nums, 0, -1)]

stack = []
answer = ""
answer_list = []
for goal in goals:
## 일단 answer가 NO가 되면 바로 끝내버리게 작성.    
    if answer != "NO":
        # inputs는 순서대로 주어졌던 수열. 수열이 존재하는동안 진행되게 loop작성
        # inputs ex) 8 7 6 5 4 3 2 1
        # 원하는 수를 출력하기 위해 inputs의 마지막 수와 비교해준다.
        # 원하는 수가 더 크다면, 원하는 수가 나오거나 inputs[-1]의 수가 더 커질때까지
        # inputs에서 pop하여 stack에 push -> '+'를 리스트에 삽입
        # ex) goal이 4라면 stack[-1]이 4가 될 때 까지
        # inputs가 비어버리면 loop를 끝낸다.
        while inputs:
            if goal > inputs[-1]:
                stack.append(inputs.pop())
                answer_list.append('+')
            elif goal == inputs[-1]:
                stack.append(inputs.pop())
                answer_list.append('+')
                break
            else:
                break
        # 루프가 끝난 후, stack 마지막(가장 최근에 들어간 것)이 goal과 같다면 pop해준다 -> 수열에 사용. 
        if stack[-1] == goal:
            stack.pop()
            answer_list.append('-')
        # 루프가 끝났는데도 stack 마지막이 goal이 아니라면 해당 수열은 만들 수가 없다.
        # 이 예시는 위의 stack에서 pop을 진행하고 나서 다음 goal로 넘어갔을 때 발생할 수 있다
        # ex) goals = [4, 2, 3, 1, 5, 6, 7, 8]
        # ex)   inputs 8 7 6 5
        #       stack 4 3 2 1 ->  4 pop
        #       stack 3 2 1 인데 원하는 2를 pop할 수가 없다. 따라서 NO!
        elif stack[-1] != goal:
            answer = "NO"
            break            
    elif answer == "NO":
        break
if answer == "NO":
    print(answer)
else:
    print("\n".join(answer_list))