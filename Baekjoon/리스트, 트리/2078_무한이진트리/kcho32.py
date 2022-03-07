x, y = map(int, input().split())
left, right = 0, 0

# while x > 1 or y > 1:
#     if x > y:
#         x -= y
#         left += 1
#     elif x < y:
#         y -= x
#         right += 1

while x > 1 or y > 1:
    if x > y:
        left += x // y
        x %= y
    else:
        right += y // x
        y %= x
# x, y가 1, 1이 되어야 root에 간거지만 둘 중 하나는 0이 나온다
# x 가 0이면 1, 1에서 (1 - y)를 한번 더 했기 때문에 (0, 1)이 나옴
# 이 말은 left가 한번 더 카운트 된 것
# y가 0일 때도 마찬가지
print(left - y, right - x)



