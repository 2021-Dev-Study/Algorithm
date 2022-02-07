def merge_sort(ary) :
    def _merge_sort(ary, l, r) :
        if l < r :
            center = (l+r) //2

            _merge_sort(ary, l, center)
            _merge_sort(ary, center+1, r)

            p = j = 0
            i = k = l

            while i <= center :
                tmp[p] = ary[i]
                p += 1
                i += 1
            while i <= r and j < p :
                if tmp[j][0] <= ary[i][0] :
                    ary[k] = tmp[j]
                    j += 1
                else :
                    ary[k] = ary[i]
                    i += 1
                k += 1
            while j < p :
                ary[k] = tmp[j]
                k += 1
                j += 1
    n = len(ary)
    tmp = [None] * n
    _merge_sort(ary, 0, (n-1))

import sys
N = int(sys.stdin.readline())
user = []
for _ in range(N) :
    n, nm = sys.stdin.readline().rstrip().split()
    user.append([int(n),nm]) # 위 sys.stdin.readline에서 int로 안해주었기 때문에
    # 꼭 int형변환 해주어야함.
# tmp = [(str(x) , y) for x, y in zip(age, name)]
merge_sort(user)
for i in range(N) :
    print(f"{user[i][0]} {user[i][1]}")

# 메모리 : 45736KB / 시간 :756ms