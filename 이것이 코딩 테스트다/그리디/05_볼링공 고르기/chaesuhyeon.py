from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

c_arr = list(combinations(arr,2))
# [(1, 3), (1, 2), (1, 3), (1, 2), (3, 2), (3, 3), (3, 2), (2, 3), (2, 2), (3, 2)] 

for i in c_arr:
    if i[0] != i[1]: # 문제에서 무게가 다른 볼링공을 고른다고 했으니까 (3,3) (2,2)같이 0번째와 1번째 숫자가 같지 않은 것만 카운트 해줌
        cnt += 1

print(cnt)
