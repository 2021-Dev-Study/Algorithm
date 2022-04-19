from collections import deque

scoville = [1, 2, 3, 9, 10, 12]
K = 7


answer = 0
food_spicy = deque(sorted(scoville))
while True:
    if len(food_spicy) == 1:
        if food_spicy.pop() < K:
            answer = -1
            break
            
    x = food_spicy.popleft()
    
    if x >= K:
        break
    else:
        x += 2 * food_spicy.popleft()
        answer += 1
        
        if x <= food_spicy[0]:
            food_spicy.appendleft(x)
        else:
            rotate_count = 0
            while True:
                if x <= food_spicy[0]:
                    food_spicy.appendleft(x)
                    food_spicy.rotate(rotate_count)
                    break
                food_spicy.rotate(-1)
                rotate_count += 1
                print(food_spicy)

