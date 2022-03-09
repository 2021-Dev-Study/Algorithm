str = input()

str_0 = str.split("0")
str_1 = str.split("1")

str_change_0 = len([x for x in str_0 if x != ""])
str_change_1 = len([x for x in str_1 if x != ""])


if str_change_0 < str_change_1:
    print(str_change_0)
else:
    print(str_change_1)