class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(3)
list.head.next = second
second.next = third
list.printList()
