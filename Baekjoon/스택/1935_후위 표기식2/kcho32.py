import sys


# for i in range(len(equ)):
#     x = equ.pop()
#     if x in "/*-+":
#         operator.append(x)
#     else:
#         nums.append(x)

# print(operator, nums)
# for i in range(n):

n = int(input())
# push pop을 위해 반대순으로 넣어줬다. pop(0)같은 경우 꺼낸 후 다른 모든 것들 또한 인덱스를  바꿔줘야하기 때문
equ = list(sys.stdin.readline().rstrip()[::-1])
nums_dict = {}
nums = []

# 각 알파벳과 숫자를 매칭해서 dictionary에 넣어준다. -> 찾을 때 더 빠르다
for i in range(n):
    nums_dict[chr(65+i)] = int(sys.stdin.readline().rstrip())

while len(equ):
    x = equ.pop()
    # equation에서 연산이 아니라면 nums 리스트에 pop한 알파벳에 해당하는 값을 넣어준다
    if x not in '/*-+':
        nums.append(nums_dict[x])
    # 연산자라면 앞에 넣었던 2개의 수를 꺼내, 먼저 꺼낸게 뒤에 오게 해서 사칙연산을 시행하고 값을 다시 nums에
    # 넣어준다
    else:
        num2 = nums.pop()
        num1 = nums.pop()
        if x == '+':
            num = num1 + num2
        elif x == '-':
            num = num1 - num2
        elif x == '*':
            num = num1 * num2
        elif x == '/':
            num = num1 / num2
        nums.append(num)
# 소수점 두자리 표현을 위해 포멧팅을 사용해서 표현해준다.
print(f'{nums[0]:.2f}')