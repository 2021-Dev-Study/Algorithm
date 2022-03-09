# str = input()

# str_0 = str.split("0")
# str_1 = str.split("1")

# str_change_0 = len([x for x in str_0 if x != ""])
# str_change_1 = len([x for x in str_1 if x != ""])


# if str_change_0 < str_change_1:
#     print(str_change_0)
# else:
#     print(str_change_1)


S = input()

cnt = 0
for i in S:
    flag = S[0]
    if i != flag:
        flag = i
        cnt += 1

print((cnt+1)//2)


# 000111 -> flag 1번 바뀜 -> 1
# 000111000 -> flag 2번 바뀜 -> 1
# 000111000111 -> flag 3번 바뀜 -> 2
# 000111000111000 -> flag 4번 바뀜 -> 2
# 000111000111000111 -> flag 5번 바뀜 -> 3
# 000111000111000111000 -> flag 6번 바뀜 -> 3