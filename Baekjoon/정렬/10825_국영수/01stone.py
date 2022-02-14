# 10825 : 국영수

n = int(input())
# n_list = []
# for _ in range(n):
#     name, kor, eng, math = map(str, input().split())
#     kor = int(kor)
#     eng = int(eng)
#     math = int(math)
#     n_list.append([name, kor, eng, math])

n_list = [input().split() for _ in range(n)]

# n_list.sort(key=lambda x: (x[1], -x[2], -x[3], x[0]))
n_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))  # kor  : 내림차순 -x[1]
                                                                      # eng  : 오름차순  x[2]
                                                                      # math : 내림차순 -x[3]
                                                                      # name : 오름차순  x[0]

for i in n_list:
    print(i[0])