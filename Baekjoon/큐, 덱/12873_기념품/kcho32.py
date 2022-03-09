# class FixedQueue:
#     class Empty(Exception):
#         pass
    
#     class Full(Exception):
#         pass

#     def __init__(self, capacity: int) -> None:
#         self.no = 0
#         self.front = 0
#         self.rear = 0
#         self.capacity = capacity
#         self.que = [None] * capacity
    
#     def __len__(self) -> int:
#         return self.no

#     def is_empty(self) -> bool:
#         return self.no <= 0
    
#     def is_full(self) -> bool:
#         return self.no >= self.capacity

#     def enque(self, x) -> None:
#         if self.is_full():
#             raise FixedQueue.Full
#         self.que[self.rear] = x
#         self.rear += 1
#         self.no += 1
#         if self.rear == self.capacity:
#             self.rear = 0

#     def deque(self):
#         if self.is_empty():
#             raise FixedQueue.Empty
#         x = self.que[self.front]
#         self.front += 1
#         self.no -= 1
#         if self.front == self.capacity:
#             self.front = 0
#         return x


# n = int(input())
# gift = FixedQueue(n)

# for i in range(1, n+1):
#     gift.enque(i)


# for i in range(1, n+1):
#     index = (i ** 3 - 1) % gift.no
#     for j in range(index):
#         gift.enque(gift.deque())
#     gift.deque()

# print(gift.que[gift.front - 1])
from collections import deque

n = int(input())
deq = deque(range(1, n+1))

# 1, n까지만 하면 덱에는 1개의 수만 남게 됨
for i in range(1, n):
    # i ** 3는 너무 큰 수가 되기 때문에
    # 원하는 수 -1 만큼 로테이트 후 pop하기.
    n_rot = (i ** 3 - 1) % len(deq)
    deq.rotate(-n_rot)
    deq.popleft()


print(deq[0])


