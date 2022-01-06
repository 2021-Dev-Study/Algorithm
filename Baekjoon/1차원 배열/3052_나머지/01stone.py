# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다.
'''
입력 : 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
      이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
출력 : 첫째 줄에, 42로 나누었을 때,
      서로 다른 나머지가 몇 개 있는지 출력한다.
'''

# num_list = []
# for i in range(10):
#     n = int(input())
#     num_list.append(n % 42)

num_list = [int(input())%42 for i in range(10)] # 10개 수를 42로 나눈 값 리스트로
print(len(set(num_list)))                       # 중복 제거하고 개수...