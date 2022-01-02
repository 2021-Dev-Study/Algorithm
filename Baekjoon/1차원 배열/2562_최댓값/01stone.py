# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 
# 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
'''
입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 
       주어지는 자연수는 100 보다 작다.
출력 : 첫째 줄에 최댓값을 출력하고, 
       둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
'''

# num_list = []
# for i in range(9):
#     num_list.append(int(input()))

num_list = [int(input()) for i in range(9)] # 9개 리스트로 넣고  

# print(max(num_list))                        # 최댓값 출력
# print(num_list.index(max(num_list))+1)      # 가장 큰 인덱스 찾고 인덱스는 0부터니까 +1 
print(max(num_list), num_list.index(max(num_list))+1)