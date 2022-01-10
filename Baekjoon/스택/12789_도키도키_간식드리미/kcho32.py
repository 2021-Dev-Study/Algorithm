import sys


n = int(sys.stdin.readline().rstrip())
line = [int(x) for x in sys.stdin.readline().rstrip().split(" ")[::-1]]
wait = []
num = 1

while True:   
    if line:
        if line[-1] == num:
            line.pop()
            num += 1
        else:
            if wait:
                if wait[-1] == num:
                    wait.pop()
                    num += 1
                else:
                    wait.append(line.pop())
            else:
                wait.append(line.pop())
        print(wait, line)
    else:
        if wait:
            if wait[-1] != num:
                break
            else:
                wait.pop()
                num += 1
        else:
            break

if not line and not wait:
    print("Nice")
else:
    print("Sad")
        
