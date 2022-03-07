class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.no = 0
        self.head = None # 제일 처음
        self.current = None # pointer
    
    def __len__(self):
        return self.no

    def add(self, num, node_data):
        # 주어진 위치가 맨 처음이 된다면 head 앞에 배치 후 노드를 새로운 head로 설정
        if self.no - num <= 0:
            node_data.next = self.head
            self.head = node_data
            self.no += 1
        # 주어진 노드의 위치를 찾고 -> index
        # 위치 1개 전까지 포인터를 옮겨주고
        # 해당 포인터 다음에 주어진 노드 주고 원래 포인터 다음은 노드 다음에 연결
        else:
            index = self.no - num
            self.current = self.head
            for i in range(index-1):
                self.current = self.current.next
            node_data.next = self.current.next
            self.current.next = node_data
            self.current = self.head
            self.no += 1
    
    def show(self):
        answer = []
        self.current = self.head
        for i in range(self.no):
            answer.append(self.current.data)
            self.current = self.current.next
        return print(" ".join(map(str, answer)))


test = LinkedList()

num = int(input())
order = list(map(int, input().split(" ")))

for i in range(num):
    test_node = Node(i+1)
    test.add(num=order[i], node_data=test_node)

test.show()
