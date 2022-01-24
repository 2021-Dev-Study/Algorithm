def card(depth):
    print("depth : " , depth)
    if depth == k:
        s.add(''.join(map(str, li)))
        print("s : ", s)
        return 
    for i in range(n):
        print(f'depth:{depth} & i:{i}')
        if check[i]:
            continue
        print("nums : ", nums)
        li.append(nums[i])
        print("li.append(nums[i]) : ", li)
        check[i] = 1
        card(depth+1)
        li.pop()
        print(f'depth:{depth} & li.pop():{li}')
        check[i] = 0
        
n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]
li, s = [], set()
check = [0]*n
card(0)
print(len(s))

# depth :  0   
# depth:0 & i:0
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1]
# depth :  1
# depth:1 & i:0 # check[0] = 1이므로 continue 
# depth:1 & i:1
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1, 2]
# depth :  2
# s :  {'12'}
# depth:1 & li.pop():[1]
# depth:1 & i:2
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1, 12]
# depth :  2
# s :  {'12', '112'}
# depth:1 & li.pop():[1]
# depth:1 & i:3
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1, 1]
# depth :  2
# s :  {'12', '11', '112'}
# depth:1 & li.pop():[1]

### 한바퀴 끝 ### 

# depth:0 & li.pop():[]
# depth:0 & i:1
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [2]
# depth :  1
# depth:1 & i:0
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [2, 1]
# depth :  2
# s :  {'12', '21', '11', '112'}
# depth:1 & li.pop():[2]
# depth:1 & i:1
# depth:1 & i:2
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [2, 12]
# depth :  2
# s :  {'21', '212', '11', '12', '112'}
# depth:1 & li.pop():[2]
# depth:1 & i:3
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [2, 1]
# depth :  2
# s :  {'21', '212', '11', '12', '112'}
# depth:1 & li.pop():[2]
# depth:0 & li.pop():[]
# depth:0 & i:2
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [12]
# depth :  1
# depth:1 & i:0
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [12, 1]
# depth :  2
# s :  {'21', '212', '11', '12', '121', '112'}
# depth:1 & li.pop():[12]
# depth:1 & i:1
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [12, 2]
# depth :  2
# s :  {'21', '212', '11', '12', '121', '112', '122'}
# depth:1 & li.pop():[12]
# depth:1 & i:2
# depth:1 & i:3
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [12, 1]
# depth :  2
# s :  {'21', '212', '11', '12', '121', '112', '122'}
# depth:1 & li.pop():[12]
# depth:0 & li.pop():[]
# depth:0 & i:3
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1]
# depth :  1
# depth:1 & i:0
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1, 1]
# depth :  2
# s :  {'21', '212', '11', '12', '121', '112', '122'}
# depth:1 & li.pop():[1]
# depth:1 & i:1
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1, 2]
# depth :  2
# s :  {'21', '212', '11', '12', '121', '112', '122'}
# depth:1 & li.pop():[1]
# depth:1 & i:2
# nums :  [1, 2, 12, 1]
# li.append(nums[i]) :  [1, 12]
# depth :  2
# s :  {'21', '212', '11', '12', '121', '112', '122'}
# depth:1 & li.pop():[1]
# depth:1 & i:3
# depth:0 & li.pop():[]