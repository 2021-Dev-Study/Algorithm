# 실패
# 반례
# 15 2
# 9 9 일때 답이 9가 나와야하는데 나오질 않음.. // IndexError 남 

def bignum(depth):
    print("depth : " , depth)
    if depth == len(str(n)):
        s.append(''.join(map(str, li)))
        print("s.append(''.join(map(str, li))) : ", s)
        if int(s[-1]) > n:
            s.pop()
        print("s : ", s)
        return 
    for i in range(k):
        print(f'depth:{depth} & i:{i}')

        print("nums : ", nums)
        li.append(nums[i])
        print("li.append(nums[i]) : ", li)

        bignum(depth+1)
        if li:
            li.pop()
        print(f'depth:{depth} & li.pop():{li}')

        
n, k = map(int, input().split())
nums = list(map(int, input().split()))
li, s = [], []

bignum(0)
s.sort()
if s:
    print(s[-1])

######## 남의 풀이 ########
# def func(order, number):
#     global max_num
#     if order == len(str(n)):
#         if not '0' in str(number):
#             max_num = max(max_num, number)
#         return
#     for i in range(k):
#         now_num = num[i] * (10 **(len(str(n))- order-1)) + number
#         if now_num <= n :
#             func(order + 1, now_num)
#         else:
#             func(order+1 , number)


# n, k = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort(reverse=True)
# max_num = 0

# func(0,0)
# print(max_num)
