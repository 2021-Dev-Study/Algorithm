def three(n, count):
    if int(n) > 9:
        count += 1
        num_list = list(n)
        num = list(map(int, num_list))
        three(str(sum(num)), count)
    else:
        print(count)
        if int(n) % 3:
            print("NO")
        else:
            print("YES")
n = input()
count = 0
three(n, count)