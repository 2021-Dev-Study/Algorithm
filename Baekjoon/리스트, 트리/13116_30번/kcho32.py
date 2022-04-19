class Node:
    def __init__(self, key=None, value=None, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None