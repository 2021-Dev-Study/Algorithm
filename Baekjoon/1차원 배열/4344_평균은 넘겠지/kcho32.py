import sys

t = int(input())
for i in range(t):
    n_stu = []
    n_stu = list(map(int, sys.stdin.readline().rstrip().split()))
    average_score = sum(n_stu[1:]) / len(n_stu[1:])
    
    def compare(score):
        return score > average_score
    
    n_stu_test = list(map(compare, n_stu[1:]))
    
    print(f'{n_stu_test.count(True)/len(n_stu_test) * 100:.3f}%')