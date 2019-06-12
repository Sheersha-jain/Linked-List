# Display a linked list from the end.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printReverse(self, node):
        if node is None:
            return
        self.printReverse(node.next)
        print("data", node.data)

list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(3)
list.head.next = second
second.next = third
n = list.head
list.printReverse(n)