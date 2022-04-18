import sys, heapq

input = sys.stdin.readline
num_of_lines, target_nums = map(int, input().split())
lines = []

for i in range(num_of_lines):
    heapq.heappush(lines, -int(input())) # 큰 수부터 가져오기 위해

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        tmp_cnt = 0

        for num in array:
            tmp_cnt += -num // mid
        if tmp_cnt == target:
            start = mid + 1
        elif tmp_cnt < target:
            end = mid - 1
        else:
            start = mid + 1
    return end # 왜 end?

end = heapq.heappop(lines)
heapq.heappush(lines, end)
# print(end)
print(binary_search(lines, target_nums, 1, -end))

