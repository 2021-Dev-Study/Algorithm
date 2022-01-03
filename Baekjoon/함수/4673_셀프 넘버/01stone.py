# 셀프넘버
'''
양의 정수 n이 주어졌을 때, 이 수를 시작해서 
n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 
'''

def d(n):                   # 생성자 함수
    n = n + sum(map(int, str(n)))
    return n

d_list = []                 # 생성자 리스트
for cnt in range(10001):
    d_list.append(d(cnt))
d_list.sort()

for cnt in range(1,10000):  # 셀프넘버 출력
    if cnt in d_list: 
        continue
    else:
        print(cnt)