# 11729 : 하노이탑
def hanoi(n, start_poll, pass_poll, goal_poll):
    if n == 1:
        print(start_poll, goal_poll)  
    else:
        hanoi(n-1, start_poll, goal_poll, pass_poll)
        print(start_poll, goal_poll)
        hanoi(n-1, pass_poll, start_poll, goal_poll)
        
n = int(input())
print(2**n - 1)
hanoi(n, 1, 2, 3)