import sys

n = int(sys.stdin.readline().rstrip())
nums: list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

################################### 버블 정렬 ########################################
# for i in range(n-1):
#     for j in range(n-1, i, -1):
#         if nums[j-1] > nums[j]:
#             nums[j-1], nums[j] = nums[j], nums[j-1]

# print("\n".join(list(map(str, nums))))

################################### 버블 정렬 (upgraded) ########################################
# 한번도 자리가 바뀌지 않았다면 모두 제 자리에 있다는 의미라서 더 이상 비교하지 않고 break
# for i in range(n-1):
#     exchng_cnt = 0
#     for j in range(n-1, i, -1):
#         if nums[j-1] > nums[j]:
#             nums[j-1], nums[j] = nums[j], nums[j-1]
#             exchng_cnt += 1
#     if not exchng_cnt:
#         break

# print("\n".join(list(map(str, nums))))

################################### 버블 정렬 (upgraded) ########################################
# 정렬 한바퀴가 끝나면 가장 왼쪽 있는 수는 이미 배치가 완료 되었기 때문에 스캔범위에서 제외
# for i in range(n-1):
#     k = 0
#     while k < n - 1:
#         last_change = n - 1
# # 뒤에서부터 비교를 하면서 마지막으로 순서가 바뀐 인덱스까지는 순서 정렬이 끝나 있는 것이라
# # 스캔 범위에서 제외
#         for j in range(n-1, k, -1):
#             if nums[j-1] > nums[j]:
#                 nums[j-1], nums[j] = nums[j], nums[j-1]
#                 last_change = j

#         k = last_change

# print("\n".join(list(map(str, nums))))

################################## 단순 선택 정렬 ####################################################
# min 인덱스의 시작은 0으로 하고 다음 인덱스부터 비교해서 더 작은 수가 나오면 min으로 바꿔준다
# for문이 끝나면 min은 실제 가장 작은 수의 인덱스이므로 정렬 안된 범위의 제일 앞으로 보내준다
# 시작은 0부터 시작해서 차근차근 작은 수를 넣어주는 정렬 

# for i in range(n-1):
#     min = i
#     for j in range(i + 1, n):
#         if nums[min] > nums[j]:
#             min = j
#     nums[min], nums[i] = nums[i], nums[min]

# print("\n".join(list(map(str, nums))))


################################## 단순 삽입 정렬 ##############################################
# for i in range(1, n):
#     tmp = nums[i]
#     j = i
    
#     while j > 0 and nums[j-1] > tmp:
#         nums[j] = nums[j-1]
#         j -= 1

#     nums[j] = tmp

# print("\n".join(list(map(str, nums))))

################################# 이진 삽입 ###################################################
for i in range(1, n):
    key = nums[i]
    pl = 0
    pr = i - 1

    while True:
        pc = (pl + pr) // 2
        if nums[pc] == key:
            break
        elif nums[pc] < key:
            pl = pc + 1
        elif nums[pc] > key:
            pr = pc - 1
        if pl > pr:
            break

    if pl <= pr:
        pd = pc + 1
    else:
        pd = pr + 1
    
    for j in range(i, pd, -1):
        nums[j] = nums[j-1]
    nums[pd] = key

print("\n".join(list(map(str, nums))))