# print whether a linked list is even or odd

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

    def evenORodd(self):
        pointer = self.head
        while(pointer is not None and pointer.next is not None):
            pointer = pointer.next.next
            if(pointer is None):
                print("list is even")
                return
        print("list is odd")


list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(39)
fourth = Node(66)
list.head.next = second
second.next = third
#third.next = fourth
list.evenORodd()