from collections import deque
n = int(input())
answer = []
for _ in range(n):
    count = 0
    record = int(input())
    left = deque(map(int, input().split(" ")))
    right = deque(map(int, input().split(" ")))
    
    for i in range(record):
        x = left[0]
        print(type(x))
        if x + 500 in left:
            if x + 1000 in right and x + 1500 in right:
                left.remove(x + 500)
                right.remove(x + 1000)
                right.remove(x + 1500)
                left.remove(x)
                count += 1
        else:
            left.rotate(-2)

    answer.append(str(count))
print("\n".join(answer))